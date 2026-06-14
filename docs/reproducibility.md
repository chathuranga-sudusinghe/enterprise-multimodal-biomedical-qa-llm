# Reproducibility

## Current Reproducible Scope

The current reproducible workflow covers repository setup, local raw-data inspection, unified QA record construction, and schema validation. It does not cover model loading, inference, training, or evaluation.

## Environment Assumptions

- Python 3.10 or later.
- A local virtual environment.
- PubMedQA and SLAKE obtained independently under terms reviewed by the human project owner.
- Raw files placed under the ignored paths expected by the inspection commands.
- Commands run from the repository root with the package installed in editable mode or `src` available on `PYTHONPATH`.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install -e .
```

On Windows PowerShell, use `.venv\Scripts\Activate.ps1` for activation.

## Safe Inspection Commands

```bash
python -m omni_clinical_llm.data.inspect_pubmedqa \
  --raw-dir data/raw/pubmedqa/source_files \
  --output artifacts/dataset_reports/pubmedqa_inspection_report.json

python -m omni_clinical_llm.data.inspect_slake \
  --raw-dir data/raw/slake/source_files \
  --output artifacts/dataset_reports/slake_inspection_report.json
```

These commands read raw local files and write JSON reports under an ignored artifacts directory.

## Test Command

```bash
python -m pytest
```

Tests were not executed during the read-only audit or this documentation remediation. The command is documented for a later approved verification task; no current pass result is claimed.

## Ignored Local State

The repository excludes virtual environments, caches, raw/interim/processed data, dataset inspection reports, model caches, adapters, and logs. This prevents accidental publication but means local execution evidence is not independently reproducible from Git alone without separately obtained datasets.

## Future Model Experiment Requirements

Each future model run should record at minimum:

- Dataset source, version, license review, access date, and checksums.
- Dataset split and preprocessing version.
- Random seed and deterministic settings.
- Foundation-model identifier and immutable checkpoint revision.
- Tokenizer or processor revision.
- Hardware, accelerator, precision, and software environment.
- Complete configuration snapshot and code commit.
- Unique run ID and timestamps.
- Adapter type, rank, target modules, and quantization metadata where applicable.
- Evaluation dataset version, metric definitions, raw outputs, and summary metrics.
- Safety review findings and known failure cases.
