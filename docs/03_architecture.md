# Architecture

The planned architecture is organized around two data tracks, a shared model layer, an evaluation layer, and a future API layer. No implementation is included in this foundation step.

## Data Track A: Text QA

1. PubMedQA.
2. Raw data inspection.
3. Schema and field validation.
4. Preprocessing decision.
5. Prompt-only baseline.
6. Fine-tuning experiments.
7. Evaluation.

Target task: biomedical research question plus PubMed abstract context to yes, no, or maybe answer with evidence-aware explanation and uncertainty or safety note.

## Data Track B: Image-Text QA

1. SLAKE.
2. Raw data inspection.
3. Image, question, and answer validation.
4. Preprocessing decision.
5. Multimodal prompt-only baseline.
6. Multimodal fine-tuning experiments.
7. Evaluation.

Target task: medical image plus question to answer with visual or evidence explanation and uncertainty or safety note.

## Model Layer

Qwen2.5-Omni is the primary model direction. Planned methods include prompt baselines, supervised fine-tuning, instruction tuning, LoRA, QLoRA, DPO, safety tuning, and later multimodal extension evaluation.

## Evaluation Layer

Evaluation will track:

- Answer accuracy.
- PubMedQA yes, no, or maybe accuracy.
- Evidence consistency.
- Visual QA accuracy.
- Visual-grounding quality.
- Hallucination checks.
- Safety compliance.
- JSON validity for structured outputs.
- Latency.
- Resource usage.

## Future API Layer

API design is planning-only for this repository phase. Future endpoints may support text biomedical QA, image medical VQA, broader multimodal health QA, and safety checks after baselines, evaluation, and fine-tuning plans are validated.
