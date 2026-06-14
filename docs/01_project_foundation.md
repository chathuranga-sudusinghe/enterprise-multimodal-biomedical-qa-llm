# Project Foundation

Omni Biomedical LLM Fine-Tuning is a research-oriented portfolio project for evidence-aware biomedical text QA and medical image-text QA. PubMedQA supports the text track, SLAKE supports the image-text track, and Qwen2.5-Omni is the proposed foundation-model direction.

## Core Objective

Build an evidence-based progression from dataset inspection and schema validation to prompt baselines, evaluated fine-tuning experiments, and documented safety analysis. The current repository implements only the inspection, validation, and unified QA record contract stages.

## Current Implementation

- PubMedQA and SLAKE inspection utilities.
- Required-field and image-path validation.
- Unified QA record builders and validator.
- Hermetic tests for the implemented utilities.
- Planning documents and disabled configuration placeholders.

No model loading, baseline inference, preprocessing pipeline, fine-tuning, or evaluation has been implemented.

## Target Users

- Biomedical AI researchers and students.
- AI and ML engineers evaluating biomedical QA workflows.
- Healthcare education and health-information teams working within non-clinical boundaries.

## Research Question

How can a future Qwen2.5-Omni-based system be evaluated and fine-tuned for evidence-aware biomedical text QA and medical image-text QA while measuring hallucination, uncertainty, and documented safety behavior?

## Current Scope

- Inspect locally obtained PubMedQA and SLAKE files.
- Preserve dataset provenance and track-specific metadata.
- Define and validate a unified QA record contract/schema.
- Document future baseline, fine-tuning, evaluation, and safety work.

## Out of Scope for the Current Stage

- Model loading, inference, training, and evaluation.
- Processed dataset generation.
- API, Docker, CI, deployment, or monitoring implementation.
- Private patient data or patient-specific clinical use.
