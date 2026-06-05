# Baseline and Evaluation Plan

Evaluation will be designed before training is implemented. Baselines and fine-tuning formats will not be finalized until real raw datasets are inspected.

## Text Baseline

The text baseline will use base Qwen2.5-Omni in prompt-only mode on PubMedQA-style input:

- Biomedical research question.
- PubMed abstract context.
- Expected yes, no, or maybe answer.
- Evidence-aware explanation.
- Uncertainty or safety note.

## Image-Text Baseline

The image-text baseline will use base Qwen2.5-Omni in prompt-only mode on SLAKE-style input:

- Medical image.
- Question.
- Expected answer.
- Visual or evidence explanation.
- Uncertainty or safety note.

## Advanced Methods

Planned methods include:

- Supervised fine-tuning.
- Instruction tuning.
- LoRA.
- QLoRA.
- DPO preference tuning.
- Safety tuning.

## Evaluation Metrics

- Yes, no, or maybe accuracy for PubMedQA.
- Answer accuracy for SLAKE.
- Explanation quality.
- Evidence consistency.
- Visual-grounding quality.
- Hallucination rate.
- Safety compliance.
- JSON validity.
- Latency.
- Resource usage.

## Comparison Plan

Compare base prompt-only behavior against SFT, LoRA, QLoRA, DPO, and safety-tuned model variants.

## Current Status

No baseline inference, evaluation code, training code, dataset files, or dataset downloads are implemented yet.
