"""Event ID epochs creation mixin for autoclean tasks.

This module provides functionality for creating epochs based on event markers in
EEG data. Event-based epochs are time segments centered around specific event markers
that represent stimuli, responses, or other experimental events of interest.

The EventIDEpochsMixin class implements methods for creating these epochs and
detecting artifacts within them, particularly focusing on reference and muscle
artifacts that can contaminate the data.

Event-based epoching is particularly useful for task-based EEG analysis, where
the data needs to be segmented around specific events of interest for further
processing and analysis, such as event-related potentials (ERPs) or time-frequency
analysis.
"""

from typing import Dict, Optional, Union

import mne
import numpy as np
import pandas as pd

from autoclean.functions.epoching import create_eventid_epochs as _create_eventid_epochs
from autoclean.utils.logging import message


class EventIDEpochsMixin:
    """Mixin class providing event ID based epochs creation functionality for EEG data."""

    def create_eventid_epochs(
        self,
        data: Union[mne.io.Raw, None] = None,
        event_id: Optional[Dict[str, int]] = None,
        tmin: float = -0.5,
        tmax: float = 2,
        baseline: Optional[tuple] = (None, 0),
        volt_threshold: Optional[Dict[str, float]] = None,
        reject_by_annotation: bool = False,
        keep_all_epochs: bool = False,
        stage_name: str = "post_epochs",
    ) -> Optional[mne.Epochs]:
        """Create epochs based on event IDs from raw data.

        Parameters
        ----------
        data : mne.io.Raw, Optional
            The raw data to create epochs from. If None, uses self.raw.
        event_id : dict, Optional
            Dictionary mapping event names to event IDs (e.g., {"target": 1, "standard": 2}).
        tmin : float, Optional
            Start time of the epoch relative to the event in seconds, by default -0.5.
        tmax : float, Optional
            End time of the epoch relative to the event in seconds, by default 2.
        baseline : tuple, Optional
            Baseline correction (tuple of start, end), by default (None, 0).
        volt_threshold : dict, Optional
            Dictionary of channel types and thresholds for rejection, by default None.
        reject_by_annotation : bool, Optional
            Whether to reject epochs by annotation, by default False.
        keep_all_epochs : bool, Optional
            If True, no epochs will be dropped - bad epochs will only be marked in metadata, by default False.
        stage_name : str, Optional
            Name for saving and metadata, by default "post_epochs".

        Returns
        -------
        epochs_clean : instance of mne.Epochs | None
            The created epochs or None if epoching is disabled.

        Notes
        -----
        This method creates epochs centered around specific event IDs in the raw data.
        It is useful for event-related potential (ERP) analysis where you want to
        extract segments of data time-locked to specific events.
        """
        # Check if epoch_settings is enabled in the configuration
        is_enabled, epoch_config = self._check_step_enabled("epoch_settings")

        if not is_enabled:
            message("info", "Epoch settings step is disabled in configuration")
            return None

        # Get epoch settings
        if epoch_config and isinstance(epoch_config, dict):
            epoch_value = epoch_config.get("value", {})
            if isinstance(epoch_value, dict):
                tmin = epoch_value.get("tmin", tmin)
                tmax = epoch_value.get("tmax", tmax)

            event_id = epoch_config.get("event_id", {})

            # Get keep_all_epochs setting if available
            keep_all_epochs = epoch_config.get("keep_all_epochs", keep_all_epochs)

            # Get baseline settings
            baseline_settings = epoch_config.get("remove_baseline", {})
            if isinstance(baseline_settings, dict) and baseline_settings.get(
                "enabled", False
            ):
                baseline = baseline_settings.get("window", baseline)

            # Get threshold settings
            threshold_settings = epoch_config.get("threshold_rejection", {})
            if isinstance(threshold_settings, dict) and threshold_settings.get(
                "enabled", False
            ):
                threshold_config = threshold_settings.get("volt_threshold", {})
                if isinstance(threshold_config, (int, float)):
                    volt_threshold = {"eeg": float(threshold_config)}
                elif isinstance(threshold_config, dict):
                    volt_threshold = {k: float(v) for k, v in threshold_config.items()}

        # Determine which data to use
        data = self._get_data_object(data)

        # Type checking
        if not isinstance(data, mne.io.Raw) and not isinstance(
            data, mne.io.base.BaseRaw
        ):
            raise TypeError("Data must be an MNE Raw object for epoch creation")

        try:
            # Check if event_id is provided
            if event_id is None:
                message("warning", "No event_id provided for event-based epoching")
                return None

            message("header", f"Creating epochs based on event IDs: {event_id}")

            # Get all events from annotations
            events_all, event_id_all = mne.events_from_annotations(data)

            # Find all event types that match our event_id values
            event_patterns = {}  # Name and code of events to epoch by
            for event_key in event_id.keys():
                # Match the event_id values with the actual event codes in the file
                matching_events = [
                    k for k in event_id_all.keys() if str(event_id[event_key]) == str(k)
                ]
                for match in matching_events:
                    event_patterns[match] = event_id_all[match]

            message(
                "info",
                f"Looking for events matching patterns: {list(event_patterns.keys())}",
            )
            # Filter events to include only those with matching trigger codes
            trigger_codes = list(event_patterns.values())

            events_trig = events_all[np.isin(events_all[:, 2], trigger_codes)]

            if len(events_trig) == 0:
                message("warning", "No matching events found")
                return None

            message("info", f"Found {len(events_trig)} events matching the patterns")

            # Create epochs with the filtered events

            # Use standalone function for core epoch creation
            epochs = _create_eventid_epochs(
                data=data,
                event_id=event_patterns,
                tmin=tmin,
                tmax=tmax,
                baseline=baseline,
                reject=(None if keep_all_epochs else volt_threshold),
                reject_by_annotation=(reject_by_annotation and not keep_all_epochs),
                preload=True,
                on_missing="ignore",  # Don't error if no events
            )

            # Step 5: Filter other events to keep only those that fall *within the kept epochs*
            sfreq = data.info["sfreq"]
            epoch_samples = epochs.events[:, 0]  # sample indices of epoch triggers

            # Compute valid ranges for each epoch (in raw sample indices)
            start_offsets = int(tmin * sfreq)
            end_offsets = int(tmax * sfreq)
            epoch_sample_ranges = [
                (s + start_offsets, s + end_offsets) for s in epoch_samples
            ]

            # Filter events_all for events that fall inside any of those ranges
            events_in_epochs = []
            for sample, prev, code in events_all:
                for i, (start, end) in enumerate(epoch_sample_ranges):
                    if start <= sample <= end:
                        events_in_epochs.append([sample, prev, code])
                        break  # prevent double counting
                    elif sample < start:
                        break

            events_in_epochs = np.array(events_in_epochs, dtype=int)
            event_descriptions = {v: k for k, v in event_id_all.items()}

            # Build metadata rows
            metadata_rows = []
            for i, (start, end) in enumerate(epoch_sample_ranges):
                epoch_events = []
                for sample, _, code in events_in_epochs:
                    if start <= sample <= end:
                        relative_time = (sample - epoch_samples[i]) / sfreq
                        label = event_descriptions.get(code, f"code_{code}")
                        epoch_events.append((label, relative_time))
                metadata_rows.append({"additional_events": epoch_events})

            # Add the metadata column
            if epochs.metadata is not None:
                epochs.metadata["additional_events"] = [
                    row["additional_events"] for row in metadata_rows
                ]
            else:
                epochs.metadata = pd.DataFrame(metadata_rows)

            # Create a copy for potential dropping
            epochs_clean = epochs.copy()

            # If we're keeping all epochs but still want to mark them, we need to apply additional logic
            if keep_all_epochs:
                # 1. Mark epochs that would have been rejected by voltage threshold
                if volt_threshold is not None:
                    # Use MNE's built-in functionality to detect which epochs exceed thresholds
                    # but don't actually drop them
                    drop_log_thresh = mne.preprocessing.compute_thresholds(
                        epochs, volt_threshold
                    )
                    bad_epochs_thresh = []

                    for idx, log in enumerate(drop_log_thresh):
                        if len(log) > 0:  # If epoch would have been dropped
                            bad_epochs_thresh.append(idx)
                            # Add to metadata which channels exceeded threshold
                            for ch_type in log:
                                col_name = f"THRESHOLD_{ch_type.upper()}"
                                if col_name not in epochs.metadata.columns:
                                    epochs.metadata[col_name] = False
                                epochs.metadata.loc[idx, col_name] = True

                    message(
                        "info",
                        f"Marked {len(bad_epochs_thresh)} epochs exceeding voltage thresholds (not dropped)",
                    )

            # If not using reject_by_annotation or keeping all epochs, manually track bad annotations
            if not reject_by_annotation or keep_all_epochs:
                # Find epochs that overlap with any "bad" or "BAD" annotations
                bad_epochs = []
                bad_annotations = {}  # To track which annotation affected each epoch

                for ann in data.annotations:
                    # Check if annotation description starts with "bad" or "BAD"
                    if ann["description"].lower().startswith("bad"):
                        ann_start = ann["onset"]
                        ann_end = ann["onset"] + ann["duration"]

                        # Check each epoch
                        for idx, event in enumerate(epochs.events):
                            epoch_start = (
                                event[0] / epochs.info["sfreq"]
                            )  # Convert to seconds
                            epoch_end = epoch_start + (tmax - tmin)

                            # Check for overlap
                            if (epoch_start <= ann_end) and (epoch_end >= ann_start):
                                bad_epochs.append(idx)

                                # Track which annotation affected this epoch
                                if idx not in bad_annotations:
                                    bad_annotations[idx] = []
                                bad_annotations[idx].append(ann["description"])

                # Remove duplicates and sort
                bad_epochs = sorted(list(set(bad_epochs)))

                # Mark bad epochs in metadata
                epochs.metadata["BAD_ANNOTATION"] = [
                    idx in bad_epochs for idx in range(len(epochs))
                ]

                # Add specific annotation types to metadata
                for idx, annotations in bad_annotations.items():
                    for annotation in annotations:
                        col_name = annotation.upper()
                        if col_name not in epochs.metadata.columns:
                            epochs.metadata[col_name] = False
                        epochs.metadata.loc[idx, col_name] = True

                message(
                    "info",
                    f"Marked {len(bad_epochs)} epochs with bad annotations (not dropped)",
                )

                # Save epochs with bad epochs marked but not dropped
                self._save_epochs_result(result_data=epochs, stage_name=stage_name)

                # Drop bad epochs only if not keeping all epochs
                if not keep_all_epochs:
                    epochs_clean.drop(bad_epochs, reason="BAD_ANNOTATION")

                    message("debug", "reordering metadata after dropping")
                    # After epochs_clean.drop(), epochs_clean.events contains the actual surviving events.
                    # epochs.metadata contains the fully augmented metadata for the original set of epochs
                    # (before this manual annotation-based drop).
                    # We need to select rows from epochs.metadata that correspond to the events
                    # actually remaining in epochs_clean.

                    if (
                        epochs_clean.metadata is not None
                    ):  # Should always be true as it's copied
                        # Get sample times of events that survived in epochs_clean
                        surviving_event_samples = epochs_clean.events[:, 0]

                        # Get sample times of the events in the original 'epochs' object
                        # (from which epochs.metadata was derived)
                        original_event_samples = epochs.events[:, 0]

                        # Find the indices in 'original_event_samples' that match 'surviving_event_samples'.
                        # This effectively maps the surviving events in epochs_clean back to their
                        # corresponding rows in the original (and fully augmented) epochs.metadata.
                        # np.isin creates a boolean mask, np.where converts it to indices.
                        kept_original_indices = np.where(
                            np.isin(original_event_samples, surviving_event_samples)
                        )[0]

                        if len(kept_original_indices) != len(epochs_clean.events):
                            message(
                                "error",
                                f"Mismatch when aligning surviving events to original metadata. "
                                f"Expected {len(epochs_clean.events)} matches, found {len(kept_original_indices)}. "
                                f"Metadata might be incorrect.",
                            )
                            # If there's a mismatch, it indicates a deeper issue, perhaps non-unique event samples
                            # or an unexpected state. For now, we proceed with potentially incorrect metadata
                            # or let MNE raise an error if lengths still don't match later.
                            # A more robust solution might involve raising an error here.

                        # Slice the augmented epochs.metadata using these derived indices.
                        # The resulting DataFrame will have the same number of rows as len(epochs_clean.events).
                        epochs_clean.metadata = epochs.metadata.iloc[
                            kept_original_indices
                        ].reset_index(drop=True)
                    else:
                        message(
                            "warning",
                            "epochs_clean.metadata was None before assignment, which is unexpected.",
                        )

            # If keeping all epochs, use the original epochs for subsequent processing
            if keep_all_epochs:
                epochs_clean = epochs
                message(
                    "info", "Keeping all epochs as requested (keep_all_epochs=True)"
                )

            # Analyze drop log to tally different annotation types
            drop_log = epochs_clean.drop_log
            total_epochs = len(drop_log)
            good_epochs = sum(1 for log in drop_log if len(log) == 0)

            # Dynamically collect all unique annotation types
            annotation_types = {}
            for log in drop_log:
                if len(log) > 0:  # If epoch was dropped
                    for annotation in log:
                        # Convert numpy string to regular string if needed
                        annotation = str(annotation)
                        annotation_types[annotation] = (
                            annotation_types.get(annotation, 0) + 1
                        )

            message("info", "\nEpoch Drop Log Summary:")
            message("info", f"Total epochs: {total_epochs}")
            message("info", f"Good epochs: {good_epochs}")
            for annotation, count in annotation_types.items():
                message("info", f"Epochs with {annotation}: {count}")

            # Add flags if needed (only if not keeping all epochs)
            if (
                not keep_all_epochs
                and (good_epochs / total_epochs) < self.EPOCH_RETENTION_THRESHOLD
            ):
                flagged_reason = (
                    f"WARNING: Only {good_epochs / total_epochs * 100}% "
                    "of epochs were kept"
                )
                self._update_flagged_status(flagged=True, reason=flagged_reason)

            # Add good and total to the annotation_types dictionary
            annotation_types["KEEP"] = good_epochs
            annotation_types["TOTAL"] = total_epochs

            # Update metadata
            metadata = {
                "duration": tmax - tmin,
                "reject_by_annotation": reject_by_annotation,
                "keep_all_epochs": keep_all_epochs,
                "initial_epoch_count": len(events_trig),
                "final_epoch_count": len(epochs_clean),
                "single_epoch_duration": epochs.times[-1] - epochs.times[0],
                "single_epoch_samples": epochs.times.shape[0],
                "initial_duration": (epochs.times[-1] - epochs.times[0])
                * len(epochs_clean),
                "numberSamples": epochs.times.shape[0] * len(epochs_clean),
                "channelCount": len(epochs.ch_names),
                "annotation_types": annotation_types,
                "marked_epochs_file": "post_epochs",
                "cleaned_epochs_file": (
                    "post_drop_bads" if not keep_all_epochs else "post_epochs"
                ),
                "tmin": tmin,
                "tmax": tmax,
                "event_id": event_id,
            }

            self._update_metadata("step_create_eventid_epochs", metadata)

            # Store epochs
            if hasattr(self, "config") and self.config.get("run_id"):
                self.epochs = epochs_clean

            # Save epochs
            if not keep_all_epochs:
                self._save_epochs_result(
                    result_data=epochs_clean, stage_name="post_drop_bad_epochs"
                )

            return epochs_clean

        except Exception as e:
            message("error", f"Error during event ID epoch creation: {str(e)}")
            raise RuntimeError(f"Failed to create event ID epochs: {str(e)}") from e
