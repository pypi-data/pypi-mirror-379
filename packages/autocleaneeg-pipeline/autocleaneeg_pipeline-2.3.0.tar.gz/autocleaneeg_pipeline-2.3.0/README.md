# AutoCleanEEG Pipeline

[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A modular framework for automated EEG data processing, built on MNE‑Python.



## Features

- Framework for automated EEG preprocessing with "lego block" modularity
- Support for multiple EEG paradigms (ASSR, Chirp, MMN, Resting State) 
- BIDS-compatible data organization and comprehensive quality control
- Extensible plugin system for file formats, montages, and event processing
- Research-focused workflow: single file testing → parameter tuning → batch processing
- Detailed output: BIDS‑compatible derivatives, single task log file, stage files, exports, and QA visualizations

## Installation (uv)

Use Astral's uv for fast, isolated installs. If you don't have uv yet, see https://docs.astral.sh/uv/

- Install CLI (recommended for users):

```bash
uv tool install autocleaneeg-pipeline
autocleaneeg-pipeline --help
```

- Upgrade or remove:

```bash
uv tool upgrade autocleaneeg-pipeline
uv tool uninstall autocleaneeg-pipeline
```

- Development install from source:

```bash
git clone https://github.com/cincibrainlab/autocleaneeg_pipeline.git
cd autoclean_pipeline
uv tool install -e --upgrade .
```

## Quick Start

Process a file using a built-in task:

```bash
autocleaneeg-pipeline process RestingEyesOpen /path/to/data.raw
```

List tasks and show overrides:

```bash
autocleaneeg-pipeline task list


## Output Structure

Each processing task writes to a self‑contained folder under your chosen output directory. The structure is designed to keep task‑level artifacts at the task root while maintaining a clean BIDS derivatives tree.

Example (per task):

```
<task>/
  bids/
    dataset_description.json
    derivatives/
      dataset_description.json
      01_import/
      02_resample/
      ...
      16_comp/
    sub-<id>/eeg/... (primary BIDS data written by mne-bids)

  exports/            # Final exported files and convenience copies (CSV/log)
  ica/                # ICA FIF files + ica_control_sheet.csv
  logs/
    pipeline.log      # Single consolidated log for all runs in this task
  qa/
    *_fastplot_summary.(tiff|png)
  reports/
    run_reports/
      *_autoclean_report.pdf
      *_processing_log.csv       # Per-file processing CSVs
      *_autoclean_report_flagged_channels.tsv

  preprocessing_log.csv          # Combined, task-level processing log (no task prefix)
```

Key points:
- Task‑root folders use concise names: `exports/`, `ica/`, `logs/`, `qa/`, `reports/`.
- Stage files go directly under `bids/derivatives/` as numbered folders (no `intermediate/`).
- No reports or per‑subject folders are created in derivatives.
- `dataset_description.json` is present at both `bids/` and `bids/derivatives/`.


## BIDS + Branding

- The BIDS `dataset_description.json` is post‑processed to:
  - Set `Name` to the task name.
  - Add `GeneratedBy` entry for `autocleaneeg-pipeline` with version.
  - Remove placeholder Authors inserted by MNE‑BIDS if present.


## Logs

- A single log file per task lives at `<task>/logs/pipeline.log`.
- Console output level matches your `--verbose` choice; file logs capture the same level.
- If you want rotation (e.g., `10 MB`), we can enable it; default is a single growing file.


## Processing Logs (CSV)

- Per‑file: `<task>/reports/run_reports/<basename>_processing_log.csv`.
- Combined (task‑level): `<task>/preprocessing_log.csv` (no taskname prefix).
- A convenience copy of the per‑file CSV is dropped into `exports/`.


## ICA Artifacts

- ICA FIF files and the editable control sheet live in `<task>/ica/`:
  - `<task>/ica/<basename>-ica.fif`
  - `<task>/ica/ica_control_sheet.csv`


## QA Visualizations

- Fastplot summary images go to `<task>/qa/`.
- The review GUI auto‑discovers images from `reports/` and `qa/`.


## Removed Legacy Folders

This release removes the old locations and naming used during development:
- No `metadata/` folder at the task root (JSONs are in `reports/run_reports/`).
- No `final_files/` or `final_exports/` (use `exports/`).
- No `ica_fif/` (use `ica/`).
- No `qa_review_plots/` (use `qa/`).
- No versioned derivatives folder (e.g., `autoclean-vX`) — derivatives are directly under `bids/derivatives/`.


## CLI Tips

- Process a single file:

```bash
autocleaneeg-pipeline process RestingEyesOpen /path/to/file.set
```

- Open the review GUI for an output directory:

```bash
autocleaneeg-pipeline review --output /path/to/output
```

- Apply ICA control‑sheet edits (reads `<task>/ica/ica_control_sheet.csv` by default when a metadata path is provided):

```bash
autocleaneeg-pipeline process ica --metadata-dir /path/to/task/reports
```
```


## Documentation

Full documentation is available at [https://docs.autocleaneeg.org](https://docs.autocleaneeg.org)

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Cincinnati Children's Hospital Research Foundation
- Built with [MNE-Python](https://mne.tools/)
