# Dataset Plan

Dataset use must be governed by licensing, source transparency, and reproducible inspection. This repository does not include dataset files and does not download datasets in the foundation phase.

## Primary Datasets

- Primary text dataset: PubMedQA.
- Primary image-text dataset: SLAKE.
- Backup image-text dataset: PathVQA.

Optional later video or audio datasets may be considered only if they are freely available, useful, and aligned with evidence-aware biomedical QA.

## Local Raw Paths

Raw data should be kept outside Git at:

- `data/raw/pubmedqa/`
- `data/raw/slake/`
- `data/raw/pathvqa/`

## Dataset Workflow

1. Download real raw data from official or license-valid sources.
2. Inspect files.
3. Inspect schema.
4. Validate columns, labels, images, and metadata.
5. Decide preprocessing.
6. Decide baseline prompts.
7. Decide fine-tuning format.

## Explicit Rule

No fake samples, no assumed schemas, no final preprocessing, no baseline design, and no training format before raw data inspection.

## Data Rules

- Do not commit raw datasets to Git.
- Do not commit secrets or access tokens.
- Check dataset licenses before use.
- Use only freely available datasets aligned with the project.
- Do not use private patient data.
