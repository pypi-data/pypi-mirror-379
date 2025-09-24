"""ICA processing functions for EEG data.

This module provides standalone functions for Independent Component Analysis (ICA)
including component fitting, classification, and artifact rejection.
"""

from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Union

import mne
import mne_icalabel
import pandas as pd
from mne.preprocessing import ICA

# Optional import for ICVision
try:
    from icvision.compat import label_components

    ICVISION_AVAILABLE = True
except ImportError:
    ICVISION_AVAILABLE = False


def fit_ica(
    raw: mne.io.Raw,
    n_components: Optional[int] = None,
    method: str = "fastica",
    max_iter: Union[int, str] = "auto",
    random_state: Optional[int] = 97,
    picks: Optional[Union[List[str], str]] = None,
    verbose: Optional[bool] = None,
    **kwargs,
) -> ICA:
    """Fit Independent Component Analysis (ICA) to EEG data.

    This function creates and fits an ICA decomposition on the provided EEG data.
    ICA is commonly used to identify and remove artifacts like eye movements,
    muscle activity, and heartbeat from EEG recordings.

    Parameters
    ----------
    raw : mne.io.Raw
        The raw EEG data to decompose with ICA.
    n_components : int or None, default None
        Number of principal components to use. If None, uses all available
        components based on the data rank.
    method : str, default "fastica"
        The ICA algorithm to use. Options: "fastica", "infomax", "picard".
    max_iter : int or "auto", default "auto"
        Maximum number of iterations for the ICA algorithm.
    random_state : int or None, default 97
        Random state for reproducible results.
    picks : list of str, str, or None, default None
        Channels to include in ICA. If None, uses all available channels.
    verbose : bool or None, default None
        Control verbosity of output.
    **kwargs
        Additional keyword arguments passed to mne.preprocessing.ICA.

    Returns
    -------
    ica : mne.preprocessing.ICA
        The fitted ICA object containing the decomposition.

    Examples
    --------
    >>> ica = fit_ica(raw)
    >>> ica = fit_ica(raw, n_components=20, method="infomax")

    See Also
    --------
    classify_ica_components : Classify ICA components using ICLabel
    apply_ica_rejection : Apply ICA to remove artifact components
    mne.preprocessing.ICA : MNE ICA implementation
    """
    # Input validation
    if not isinstance(raw, mne.io.BaseRaw):
        raise TypeError(f"Data must be an MNE Raw object, got {type(raw).__name__}")

    if method not in ["fastica", "infomax", "picard"]:
        raise ValueError(
            f"method must be 'fastica', 'infomax', or 'picard', got '{method}'"
        )

    if n_components is not None and n_components <= 0:
        raise ValueError(f"n_components must be positive, got {n_components}")

    try:
        # Remove 'ortho' from fit_params if method is 'infomax' and 'ortho' is in kwargs
        if (
            method == "infomax"
            and "fit_params" in kwargs
            and "ortho" in kwargs["fit_params"]
        ):
            kwargs["fit_params"].pop("ortho")

        if verbose:
            print(f"Running ICA with method: '{method}'")

        # Create ICA object
        ica_kwargs = {
            "n_components": n_components,
            "method": method,
            "max_iter": max_iter,
            "random_state": random_state,
            **kwargs,
        }

        ica = ICA(**ica_kwargs)

        # Fit ICA to the data
        ica.fit(raw, picks=picks, verbose=verbose)

        return ica

    except Exception as e:
        raise RuntimeError(f"Failed to fit ICA: {str(e)}") from e


def classify_ica_components(
    raw: mne.io.Raw,
    ica: ICA,
    method: str = "iclabel",
    verbose: Optional[bool] = None,
    **kwargs,
) -> pd.DataFrame:
    """Classify ICA components using automated algorithms.

    This function uses automated classification methods to identify the likely
    source of each ICA component (brain, eye, muscle, heart, etc.). Supports
    both ICLabel and ICVision methods for component classification.

    Parameters
    ----------
    raw : mne.io.Raw
        The raw EEG data used for ICA fitting.
    ica : mne.preprocessing.ICA
        The fitted ICA object to classify.
    method : str, default "iclabel"
        Classification method to use. Options: "iclabel", "icvision", "hybrid".
    verbose : bool or None, default None
        Control verbosity of output.
    **kwargs
        Additional keyword arguments passed to the classification method.
        For icvision-related methods, supports 'psd_fmax' to limit PSD plot
        frequency range. For the ``hybrid`` method, ``icvision_n_components``
        controls how many leading components are reclassified with ICVision.

    Returns
    -------
    component_labels : pd.DataFrame
        DataFrame with columns:
        - "component": Component index
        - "ic_type": Predicted component type (brain, eye, muscle, etc.)
        - "confidence": Confidence score (0-1) for the prediction
        - Additional columns with probabilities for each component type

    Examples
    --------
    >>> labels = classify_ica_components(raw, ica, method="iclabel")
    >>> labels = classify_ica_components(raw, ica, method="icvision")
    >>> labels = classify_ica_components(raw, ica, method="hybrid", icvision_n_components=15)
    >>> artifacts = labels[(labels["ic_type"] == "eye") & (labels["confidence"] > 0.8)]

    See Also
    --------
    fit_ica : Fit ICA decomposition to EEG data
    apply_ica_rejection : Apply ICA to remove artifact components
    mne_icalabel.label_components : ICLabel implementation
    """
    # Input validation
    if not isinstance(raw, mne.io.BaseRaw):
        raise TypeError(f"Raw data must be an MNE Raw object, got {type(raw).__name__}")

    if not isinstance(ica, ICA):
        raise TypeError(f"ICA must be an MNE ICA object, got {type(ica).__name__}")

    if method not in ["iclabel", "icvision", "hybrid"]:
        raise ValueError(
            f"method must be 'iclabel', 'icvision', or 'hybrid', got '{method}'"
        )

    try:
        if method == "iclabel":
            # Run ICLabel classification
            mne_icalabel.label_components(raw, ica, method="iclabel")
            # Extract results into a DataFrame
            component_labels = _icalabel_to_dataframe(ica)
            component_labels = _attach_source_metadata(
                component_labels,
                iclabel_df=component_labels.copy(),
                icvision_df=None,
            )

        elif method == "icvision":
            # Run ICVision classification
            if not ICVISION_AVAILABLE:
                raise ImportError(
                    "autoclean-icvision package is required for icvision method. "
                    "Install it with: pip install autoclean-icvision"
                )

            # Use ICVision as drop-in replacement, passing through any extra kwargs
            label_components(raw, ica, **kwargs)
            # Extract and tag results as ICVision outputs
            component_labels = _icalabel_to_dataframe(ica)
            component_labels["annotator"] = "ic_vision"
            component_labels = _attach_source_metadata(
                component_labels,
                iclabel_df=None,
                icvision_df=component_labels.copy(),
            )

        elif method == "hybrid":
            # First run ICLabel on all components (produces full-size labels/scores)
            mne_icalabel.label_components(raw, ica, method="iclabel")

            if not ICVISION_AVAILABLE:
                raise ImportError(
                    "autoclean-icvision package is required for hybrid method. "
                    "Install it with: pip install autoclean-icvision"
                )

            # Preserve ICLabel results so we can merge with ICVision outputs
            try:
                import numpy as _np  # local import to avoid hard dep at module import
            except Exception:  # pragma: no cover - numpy is a strong dep in env
                raise RuntimeError(
                    "NumPy is required for hybrid ICA classification merge logic"
                )

            iclabel_df = _icalabel_to_dataframe(ica).copy()

            n_comp = ica.n_components_
            # Copy ICLabel per-class probabilities and label mapping
            iclabel_scores = (
                _np.array(ica.labels_scores_, copy=True)
                if hasattr(ica, "labels_scores_")
                else None
            )
            iclabel_labels_dict = {k: list(v) for k, v in getattr(ica, "labels_", {}).items()}

            # Determine which leading components to reclassify with ICVision
            icvision_n_components = kwargs.pop("icvision_n_components", 20)
            component_indices = list(range(min(icvision_n_components, n_comp)))

            # Run ICVision on the subset; this may overwrite ica.labels_/labels_scores_
            label_components(raw, ica, component_indices=component_indices, **kwargs)

            # Prepare containers for vision-only metadata
            vision_ic_type = [None] * n_comp
            vision_confidence = [_np.nan] * n_comp

            # Build merged per-component label list starting from ICLabel then overlay ICVision
            merged_ic_type = [""] * n_comp
            # Fill from ICLabel first
            for lbl, comps in iclabel_labels_dict.items():
                for ci in comps:
                    if 0 <= ci < n_comp:
                        merged_ic_type[ci] = lbl
            # Overlay ICVision labels for the processed subset (as provided by icvision)
            icvision_labels_dict = {k: list(v) for k, v in getattr(ica, "labels_", {}).items()}
            for lbl, comps in icvision_labels_dict.items():
                for ci in comps:
                    if 0 <= ci < n_comp:
                        merged_ic_type[ci] = lbl
                        vision_ic_type[ci] = lbl

            # Build merged confidence matrix: start from ICLabel scores, then replace subset rows with ICVision
            # If ICLabel didn't provide scores, initialize to ones
            if iclabel_scores is None or (
                hasattr(iclabel_scores, "shape") and iclabel_scores.shape[0] != n_comp
            ):
                # Initialize with 1.0 confidence for lack of better info
                merged_scores = _np.ones((n_comp, 7), dtype=float)
            else:
                merged_scores = iclabel_scores.copy()

            # If ICVision provided per-class scores for the subset, overlay them
            icvision_scores = getattr(ica, "labels_scores_", None)
            if icvision_scores is not None:
                icvision_scores = _np.array(icvision_scores, copy=False)
                # If sizes match the subset length, assume row order corresponds to component_indices
                if icvision_scores.ndim == 2 and icvision_scores.shape[0] == len(component_indices):
                    for row_idx, comp_idx in enumerate(component_indices):
                        if 0 <= comp_idx < n_comp:
                            max_prob = float(icvision_scores[row_idx].max())
                            vision_confidence[comp_idx] = max_prob
                            # Ensure number of classes aligns; if not, take max prob only
                            if icvision_scores.shape[1] == merged_scores.shape[1]:
                                merged_scores[comp_idx, :] = icvision_scores[row_idx, :]
                            else:
                                # Fallback: keep existing distribution but update max/confidence
                                merged_scores[comp_idx, :] = max_prob
                else:
                    # If shape is unexpected, at least try to update confidence for the subset
                    if icvision_scores.ndim == 2:
                        max_probs = icvision_scores.max(axis=1)
                        for row_idx, comp_idx in enumerate(component_indices[: len(max_probs)]):
                            if 0 <= comp_idx < n_comp:
                                max_prob = float(max_probs[row_idx])
                                vision_confidence[comp_idx] = max_prob
                                merged_scores[comp_idx, :] = max_prob

            # Update the ICA object with merged labels and scores so downstream code sees full arrays
            # Rebuild labels_ dict from merged_ic_type
            merged_labels_dict: Dict[str, List[int]] = {}
            for ci, lbl in enumerate(merged_ic_type):
                merged_labels_dict.setdefault(lbl, []).append(ci)
            ica.labels_ = merged_labels_dict
            ica.labels_scores_ = merged_scores

            # Extract combined results as DataFrame
            component_labels = _icalabel_to_dataframe(ica)
            # Mark which components were reclassified by ICVision for downstream reporting
            if component_indices:
                component_labels.loc[component_indices, "annotator"] = "ic_vision"

            vision_df = pd.DataFrame(
                {
                    "component": getattr(ica, "_ica_names", list(range(n_comp))),
                    "annotator": ["ic_vision"] * n_comp,
                    "ic_type": vision_ic_type,
                    "confidence": vision_confidence,
                },
                index=range(n_comp),
            )

            component_labels = _attach_source_metadata(
                component_labels,
                iclabel_df=iclabel_df,
                icvision_df=vision_df,
            )

        return component_labels

    except Exception as e:
        raise RuntimeError(
            f"Failed to classify ICA components with {method}: {str(e)}"
        ) from e


def apply_ica_rejection(
    raw: mne.io.Raw,
    ica: ICA,
    components_to_reject: List[int],
    copy: bool = True,
    verbose: Optional[bool] = None,
) -> mne.io.Raw:
    """Apply ICA to remove specified components from EEG data.

    This function applies the ICA transformation to remove specified artifact
    components from the EEG data, effectively cleaning the signal.

    Parameters
    ----------
    raw : mne.io.Raw
        The raw EEG data to clean.
    ica : mne.preprocessing.ICA
        The fitted ICA object.
    components_to_reject : list of int
        List of component indices to remove from the data.
    copy : bool, default True
        If True, returns a copy of the data. If False, modifies in place.
    verbose : bool or None, default None
        Control verbosity of output.

    Returns
    -------
    raw_cleaned : mne.io.Raw
        The cleaned EEG data with artifact components removed.

    Examples
    --------
    >>> raw_clean = apply_ica_rejection(raw, ica, [0, 2, 5])

    See Also
    --------
    fit_ica : Fit ICA decomposition to EEG data
    classify_ica_components : Classify ICA components
    mne.preprocessing.ICA.apply : Apply ICA transformation
    """
    # Input validation
    if not isinstance(raw, mne.io.BaseRaw):
        raise TypeError(f"Raw data must be an MNE Raw object, got {type(raw).__name__}")

    if not isinstance(ica, ICA):
        raise TypeError(f"ICA must be an MNE ICA object, got {type(ica).__name__}")

    if not isinstance(components_to_reject, list):
        components_to_reject = list(components_to_reject)

    # Validate component indices
    max_components = ica.n_components_
    invalid_components = [
        c for c in components_to_reject if c < 0 or c >= max_components
    ]
    if invalid_components:
        raise ValueError(
            f"Invalid component indices {invalid_components}. "
            f"Must be between 0 and {max_components - 1}"
        )

    try:
        # Set components to exclude - simple approach matching original mixin
        ica_copy = ica.copy()
        ica_copy.exclude = components_to_reject

        # Apply ICA
        raw_cleaned = ica_copy.apply(raw, copy=copy, verbose=verbose)

        return raw_cleaned

    except Exception as e:
        raise RuntimeError(f"Failed to apply ICA rejection: {str(e)}") from e


def _icalabel_to_dataframe(ica: ICA) -> pd.DataFrame:
    """Convert ICLabel results to a pandas DataFrame.

    Helper function to extract ICLabel classification results from an ICA object
    and format them into a convenient DataFrame structure.

    This matches the format used in the original AutoClean ICA mixin.
    """
    # Initialize ic_type array with empty strings
    ic_type = [""] * ica.n_components_

    # Fill in the component types based on labels
    for label, comps in ica.labels_.items():
        for comp in comps:
            ic_type[comp] = label

    # Create DataFrame matching the original format with component index as DataFrame index
    results = pd.DataFrame(
        {
            "component": getattr(ica, "_ica_names", list(range(ica.n_components_))),
            "annotator": ["ic_label"] * ica.n_components_,
            "ic_type": ic_type,
            "confidence": (
                ica.labels_scores_.max(1)
                if hasattr(ica, "labels_scores_")
                else [1.0] * ica.n_components_
            ),
        },
        index=range(ica.n_components_),
    )  # Ensure index is component indices

    return results


def _series_from_df(
    df: Optional[pd.DataFrame],
    column: str,
    index: pd.Index,
    *,
    fill_value: Optional[Union[float, str]] = None,
    dtype: Optional[Union[str, type]] = None,
) -> pd.Series:
    """Helper to safely extract a column aligned to the provided index."""
    if df is None or column not in df.columns:
        values = [fill_value] * len(index)
        return pd.Series(values, index=index, dtype=dtype)
    series = df[column].reindex(index)
    return series


def _attach_source_metadata(
    base_df: pd.DataFrame,
    *,
    iclabel_df: Optional[pd.DataFrame],
    icvision_df: Optional[pd.DataFrame],
) -> pd.DataFrame:
    """Augment classification results with source-specific metadata."""
    aligned_iclabel = iclabel_df.reindex(base_df.index).copy() if iclabel_df is not None else None
    aligned_icvision = (
        icvision_df.reindex(base_df.index).copy() if icvision_df is not None else None
    )

    if aligned_iclabel is not None and "annotator" not in aligned_iclabel.columns:
        aligned_iclabel["annotator"] = "ic_label"

    if aligned_icvision is not None:
        if "annotator" not in aligned_icvision.columns:
            aligned_icvision["annotator"] = "ic_vision"
        if aligned_iclabel is not None:
            missing_type = aligned_icvision["ic_type"].isna() | (aligned_icvision["ic_type"] == "")
            aligned_icvision.loc[missing_type, "ic_type"] = aligned_iclabel.loc[
                missing_type, "ic_type"
            ]
            if "confidence" in aligned_icvision.columns and "confidence" in aligned_iclabel.columns:
                missing_conf = aligned_icvision["confidence"].isna()
                aligned_icvision.loc[missing_conf, "confidence"] = aligned_iclabel.loc[
                    missing_conf, "confidence"
                ]

    augmented = base_df.copy()
    idx = augmented.index
    augmented["iclabel_ic_type"] = _series_from_df(
        aligned_iclabel, "ic_type", idx, fill_value=None, dtype=object
    )
    augmented["iclabel_confidence"] = _series_from_df(
        aligned_iclabel, "confidence", idx, fill_value=float("nan"), dtype=float
    )
    augmented["icvision_ic_type"] = _series_from_df(
        aligned_icvision, "ic_type", idx, fill_value=None, dtype=object
    )
    augmented["icvision_confidence"] = _series_from_df(
        aligned_icvision, "confidence", idx, fill_value=float("nan"), dtype=float
    )

    attrs: Dict[str, pd.DataFrame] = {}
    if aligned_iclabel is not None:
        attrs["iclabel_df"] = aligned_iclabel
    if aligned_icvision is not None:
        attrs["icvision_df"] = aligned_icvision
    augmented.attrs = attrs

    return augmented


def apply_ica_component_rejection(
    raw: mne.io.Raw,
    ica: ICA,
    labels_df: pd.DataFrame,
    ic_flags_to_reject: List[str] = ["eog", "muscle", "ecg"],
    ic_rejection_threshold: float = 0.8,
    ic_rejection_overrides: Optional[Dict[str, float]] = None,
    verbose: Optional[bool] = None,
) -> tuple[mne.io.Raw, List[int]]:
    """Apply ICA rejection based on component classifications and criteria.

    This function combines the classification results with rejection criteria
    to automatically identify and remove artifact components. Works with both
    ICLabel and ICVision classification results.

    Parameters
    ----------
    raw : mne.io.Raw
        The raw EEG data to clean.
    ica : mne.preprocessing.ICA
        The fitted ICA object with component classifications.
    labels_df : pd.DataFrame
        DataFrame with classification results from classify_ica_components().
    ic_flags_to_reject : list of str, default ["eog", "muscle", "ecg"]
        Component types to consider for rejection.
    ic_rejection_threshold : float, default 0.8
        Global confidence threshold for rejecting components.
    ic_rejection_overrides : dict of str to float, optional
        Per-component-type confidence thresholds that override the global threshold.
        Keys are IC types (e.g., 'muscle', 'heart'), values are confidence thresholds.
    verbose : bool or None, default None
        Control verbosity of output.

    Returns
    -------
    raw_cleaned : mne.io.Raw
        The cleaned EEG data with artifact components removed.
    rejected_components : list of int
        List of component indices that were rejected.

    Examples
    --------
    >>> raw_clean, rejected = apply_ica_component_rejection(raw, ica, labels)

    See Also
    --------
    fit_ica : Fit ICA decomposition to EEG data
    classify_ica_components : Classify ICA components
    apply_ica_rejection : Apply ICA to remove specific components
    """
    # Find components that meet rejection criteria - use DataFrame index like original mixin
    if ic_rejection_overrides is None:
        ic_rejection_overrides = {}

    rejected_components = []
    for idx, row in labels_df.iterrows():
        ic_type = row["ic_type"]
        confidence = row["confidence"]

        if ic_type in ic_flags_to_reject:
            # Use override threshold if available, otherwise global threshold
            threshold = ic_rejection_overrides.get(ic_type, ic_rejection_threshold)

            if confidence > threshold:
                rejected_components.append(idx)

    # Match original mixin logic exactly
    if not rejected_components:
        if verbose:
            print("No new components met rejection criteria in this step.")
        return raw, rejected_components
    else:
        if verbose:
            print(
                f"Identified {len(rejected_components)} components for rejection: {rejected_components}"
            )

        # Combine with any existing exclusions like original mixin
        ica_copy = ica.copy()
        if ica_copy.exclude is None:
            ica_copy.exclude = []

        current_exclusions = set(ica_copy.exclude)
        for idx in rejected_components:
            current_exclusions.add(idx)
        ica_copy.exclude = sorted(list(current_exclusions))

        # Also update the original ICA object so the mixin can access the excluded components
        ica.exclude = ica_copy.exclude.copy()

        if verbose:
            print(f"Total components now marked for exclusion: {ica_copy.exclude}")

        if not ica_copy.exclude:
            if verbose:
                print("No components are marked for exclusion. Skipping ICA apply.")
            return raw, rejected_components
        else:
            # Apply ICA to remove the excluded components (modifies in place like original mixin)
            ica_copy.apply(raw, verbose=verbose)
            if verbose:
                print(
                    f"Applied ICA, removing/attenuating {len(ica_copy.exclude)} components."
                )

    return raw, rejected_components


def _parse_component_str(value: str) -> set[int]:
    """Parse a comma-separated component string into a set of ints."""
    if value is None or str(value).strip() == "" or pd.isna(value):
        return set()
    return {int(item) for item in str(value).split(",") if item.strip().isdigit()}


def _format_component_list(values: List[int]) -> str:
    """Format a list of component integers as a comma-separated string."""
    return ",".join(str(v) for v in values)


def update_ica_control_sheet(
    autoclean_dict: Dict[str, Union[str, Path]], auto_exclude: List[int]
) -> List[int]:
    """Update the ICA control sheet and return the final exclusion list.

    Parameters
    ----------
    autoclean_dict : dict
        Configuration dictionary containing at minimum ``metadata_dir``,
        ``derivatives_dir`` and ``unprocessed_file`` keys.
    auto_exclude : list of int
        Components automatically selected for exclusion in the current run.

    Returns
    -------
    list of int
        Final list of components to exclude after applying manual edits from
        the control sheet.
    """

    # Resolve ICA directory under task root
    ica_dir_cfg = autoclean_dict.get("ica_dir")
    if ica_dir_cfg:
        ica_root = Path(ica_dir_cfg)
    else:
        reports_dir = autoclean_dict.get("reports_dir")
        bids_dir = autoclean_dict.get("bids_dir")
        if reports_dir:
            ica_root = Path(reports_dir).parent / "ica"
        elif bids_dir:
            ica_root = Path(bids_dir).parent / "ica"
        else:
            raise ValueError("Cannot determine ICA directory: missing 'ica_dir', 'reports_dir', and 'bids_dir'")
    ica_root.mkdir(parents=True, exist_ok=True)
    sheet_path = ica_root / "ica_control_sheet.csv"

    original_file = Path(autoclean_dict["unprocessed_file"]).name
    ica_fif = ica_root / f"{Path(original_file).stem}-ica.fif"
    auto_initial_str = _format_component_list(sorted(auto_exclude))
    now_iso = datetime.now().isoformat()

    columns = [
        "original_file",
        "ica_fif",
        "auto_initial",
        "final_removed",
        "manual_add",
        "manual_drop",
        "status",
        "last_run_iso",
    ]

    if sheet_path.exists():
        df = pd.read_csv(sheet_path, dtype=str, keep_default_na=False)
    else:
        df = pd.DataFrame(columns=columns)

    if original_file not in df.get("original_file", []).tolist():
        # First run for this file: create new row with auto selections
        new_row = {
            "original_file": original_file,
            "ica_fif": str(ica_fif),
            "auto_initial": auto_initial_str,
            "final_removed": auto_initial_str,
            "manual_add": "",
            "manual_drop": "",
            "status": "auto",
            "last_run_iso": now_iso,
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(sheet_path, index=False)
        return sorted(auto_exclude)

    # Existing row: apply manual edits if present
    idx = df.index[df["original_file"] == original_file][0]

    final_removed_set = _parse_component_str(df.loc[idx, "final_removed"])
    manual_add_set = _parse_component_str(df.loc[idx, "manual_add"])
    manual_drop_set = _parse_component_str(df.loc[idx, "manual_drop"])

    if manual_add_set or manual_drop_set:
        final_removed_set = (final_removed_set | manual_add_set) - manual_drop_set
        df.loc[idx, "final_removed"] = _format_component_list(sorted(final_removed_set))
        df.loc[idx, "manual_add"] = ""
        df.loc[idx, "manual_drop"] = ""
        df.loc[idx, "status"] = (
            "auto"
            if df.loc[idx, "auto_initial"] == df.loc[idx, "final_removed"]
            else "applied"
        )

    # Always update paths and timestamp
    df.loc[idx, "ica_fif"] = str(ica_fif)
    df.loc[idx, "last_run_iso"] = now_iso

    df.to_csv(sheet_path, index=False)

    return sorted(final_removed_set)
