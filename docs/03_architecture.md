# Architecture

The repository currently implements a data-utility layer and documents later model and evaluation layers. Placeholder package directories do not represent working runtime components.

## Implemented Data Layer

### PubMedQA Text Track

1. Read locally obtained JSONL configurations.
2. Inspect columns, counts, labels, missing fields, and text-length statistics.
3. Build a unified biomedical text QA record from an already loaded record.
4. Validate the shared and text-specific schema requirements.

### SLAKE Image-Text Track

1. Read locally obtained train, validation, and test JSON files.
2. Inspect columns, distributions, missing fields, and referenced image paths.
3. Build a unified medical visual QA record from an already loaded record and image path.
4. Validate the shared and image-text-specific schema requirements.

## Unified QA Record Contract

Both tracks use `task_type`, `instruction`, `input`, `target`, and `metadata`. This is image-text schema preparation, not a completed preprocessing pipeline or multimodal fine-tuning system.

## Proposed Model Layer

Qwen2.5-Omni is the proposed foundation-model direction. Prompt baselines, SFT, LoRA, QLoRA, DPO, safety tuning, and multimodal training are planned and not implemented.

## Planned Evaluation Layer

Future evaluation may measure answer accuracy, evidence consistency, visual grounding, hallucination, safety behavior, structured-output validity, latency, and resource usage. No evaluation runner or results exist.

## Deferred Service Layer

An API or deployment layer is not part of the current implementation. It should be reconsidered only after reproducible baselines and evaluation evidence exist.
