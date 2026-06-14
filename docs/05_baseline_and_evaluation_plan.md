# Baseline and Evaluation Plan

Everything in this document is planned. No model has been loaded, no baseline inference has been executed, and no evaluation result exists.

## Proposed Foundation-Model Direction

Qwen2.5-Omni is the proposed direction for future text and image-text experiments. The exact model revision, processor, hardware requirements, and license terms must be reviewed before integration.

## Planned Prompt-Only Baselines

- PubMedQA: question and supplied abstract context to a bounded answer and yes/no/maybe label where applicable.
- SLAKE: referenced medical image and question to a bounded answer.

Baseline prompts, decoding settings, structured outputs, and refusal behavior must be versioned before execution.

## Planned Fine-Tuning Methods

- Supervised fine-tuning and instruction tuning.
- LoRA and QLoRA.
- DPO only with documented preference-data provenance.
- Safety tuning only with measurable safety evaluation.

These methods are alternatives for staged experiments, not completed capabilities.

## Planned Evaluation

- PubMedQA yes/no/maybe accuracy where labels support it.
- SLAKE answer accuracy by split and language.
- Evidence consistency and visual-grounding analysis.
- Hallucination and uncertainty behavior.
- Safety-boundary behavior.
- Structured-output validity.
- Latency and resource usage.

## Planned Comparison Sequence

1. Base prompt-only behavior.
2. SFT baseline.
3. LoRA or QLoRA variants justified by resource constraints.
4. DPO or safety-tuned variants only after earlier evidence exists.

No comparison should be claimed without versioned configuration, immutable model revision, dataset provenance, raw outputs, metric definitions, and reproducible run metadata.
