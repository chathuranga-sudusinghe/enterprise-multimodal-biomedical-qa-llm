# Omni Biomedical LLM Fine-Tuning

Research-oriented biomedical QA fine-tuning portfolio project. Current implementation includes PubMedQA and SLAKE dataset inspection, validation, and a unified text/image QA schema. Model baseline, QLoRA fine-tuning, and evaluation are the next implementation stages.

Qwen2.5-Omni is the proposed foundation-model direction. No model has been loaded, trained, or evaluated in this repository.

## Project Objective

Build a reproducible path toward evidence-aware biomedical text QA and medical image-text QA while preserving dataset provenance, documenting safety boundaries, and separating implemented work from future experiments.

## Current Status

### Implemented

- PubMedQA JSONL inspection and required-field validation.
- SLAKE split inspection, required-field validation, and image-path checks.
- Unified QA record builders for text and image-text examples.
- Validation of the shared `task_type`, `instruction`, `input`, `target`, and `metadata` contract.
- Hermetic unit tests using temporary synthetic fixtures.
- Configuration placeholders with model loading, training, and evaluation disabled.

### Locally Executed

- Ignored local inspection reports exist for PubMedQA and SLAKE.
- These reports are not committed and therefore are not public execution evidence.
- Tests were not executed during the credibility audit or this remediation task.

### Planned, Not Yet Implemented

- Qwen2.5-Omni model loading and prompt-only baselines.
- Deterministic end-to-end preprocessing and versioned processed datasets.
- Supervised fine-tuning, LoRA, QLoRA, DPO, and safety-tuning experiments.
- Multimodal training and model evaluation.
- API, Docker, CI, deployment, and monitoring capabilities.

See [Current Project Status](docs/current_project_status.md) for the complete capability matrix.

## Dataset Roles

- **PubMedQA:** biomedical text QA grounded in supplied research abstract context.
- **SLAKE:** medical image-text QA grounded in a referenced medical image.

Both datasets are expected to be obtained and stored locally. Dataset access, licensing, and redistribution terms must be verified by the human project owner before use or publication. See [Data Card](docs/data_card.md).

## Repository Structure

```text
configs/                         Configuration placeholders and safety boundaries
docs/                            Project design and status documentation
src/omni_clinical_llm/data/     Dataset inspectors and unified QA schema helpers
src/omni_clinical_llm/          Placeholder packages for future project stages
tests/                           Hermetic tests for current utilities and structure
```

Local `data/` and generated `artifacts/` content are excluded from Git.

## Setup

Python 3.10 or later is required.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install -e .
```

On Windows PowerShell, activate the environment with `.venv\Scripts\Activate.ps1`.

The requirements file includes dependencies reserved for later stages. Installing it does not imply that API, model, training, or evaluation capabilities are implemented.

## Safe Data Inspection

After obtaining the datasets under the expected ignored local paths:

```bash
python -m omni_clinical_llm.data.inspect_pubmedqa \
  --raw-dir data/raw/pubmedqa/source_files \
  --output artifacts/dataset_reports/pubmedqa_inspection_report.json

python -m omni_clinical_llm.data.inspect_slake \
  --raw-dir data/raw/slake/source_files \
  --output artifacts/dataset_reports/slake_inspection_report.json
```

These commands read local dataset files and write ignored summary reports. Review dataset terms before downloading, inspecting, or publishing any material.

## Testing

The repository contains tests for inspectors, schema builders, validation behavior, and project structure:

```bash
python -m pytest
```

Tests were not executed during the credibility audit or this remediation task. No current pass result is claimed here.

## Planned Fine-Tuning Roadmap

1. Confirm dataset sources, versions, licenses, checksums, and access records.
2. Implement deterministic conversion into the unified QA record contract.
3. Define and execute prompt-only text and image-text baselines.
4. Add evaluation code and versioned experiment configuration.
5. Run reviewed SFT, LoRA, and QLoRA experiments.
6. Consider DPO, safety tuning, and broader multimodal work only after baseline evidence exists.

## Safety and Intended Use

This repository is for research and educational engineering work. Safety boundaries are documented, but no model-level safety enforcement or clinical validation exists.

The project is not intended for diagnosis, treatment selection, prescription guidance, patient-specific advice, or autonomous clinical decisions. It must not replace qualified medical professionals.

## Known Limitations

- No model has been loaded, trained, fine-tuned, or evaluated.
- No baseline inference, adapters, checkpoints, metrics, or comparison reports exist.
- Image-path schema preparation is not multimodal training.
- Audio and video remain future scope only.
- Reproducibility currently covers data utilities, not model experiments.

See [Limitations](docs/limitations.md) and [Reproducibility](docs/reproducibility.md).

## Licensing and Third-Party Assets

Repository-authored code and documentation are licensed under the [Apache License 2.0](LICENSE). This license does not grant rights to PubMedQA, SLAKE, Qwen2.5-Omni model weights, or any other third-party dataset or model asset. Their terms must be reviewed separately before access, use, redistribution, or publication.

## AI-Assisted Development

The project includes reviewed AI-assisted planning, implementation, debugging, and documentation work. Human decisions control architecture, safety boundaries, dataset handling, and final claims. See [AI Usage](AI_USAGE.md).
