# Architecture

The initial architecture is organized around separate concerns for data handling, inference, evaluation, training, and governance.

## Planned Components

- `data`: Dataset validation, metadata handling, preprocessing, and de-identification checks.
- `inference`: Baseline model interaction and clinician-facing support workflows.
- `evaluation`: Documentation quality, summarization quality, missing-information detection, and safety evaluation.
- `training`: Future fine-tuning configuration and experiment orchestration.
- `governance`: Safety policies, audit requirements, compliance notes, and review gates.

## Current Status

Only the repository foundation is implemented. Component directories are placeholders for future work.
