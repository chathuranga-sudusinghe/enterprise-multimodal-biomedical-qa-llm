# System Scope

The project is a research-oriented biomedical QA fine-tuning portfolio. Qwen2.5-Omni is the proposed foundation-model direction; it has not been integrated.

## Implemented Scope

- PubMedQA text QA inspection and validation.
- SLAKE image-text QA inspection and validation.
- Unified QA record construction and schema validation.
- Dataset, evaluation, and safety planning.

## Planned Scope

- Prompt-only text and image-text baselines.
- Deterministic preprocessing with versioned local outputs.
- Supervised fine-tuning, instruction tuning, LoRA, and QLoRA experiments.
- DPO and safety tuning only after suitable data and evaluation design exist.
- Evaluation of answer quality, evidence consistency, visual grounding, hallucination, safety behavior, structured-output validity, latency, and resource use.

## Not Implemented

- Model loading, inference, training, or evaluation.
- Multimodal training.
- API services, Docker, CI, deployment, or monitoring.

## Out of Scope

- Patient-specific diagnosis or autonomous clinical decisions.
- Treatment or prescription advice.
- Replacement for medical professionals.
- Private patient data or restricted clinical records.
- Hospital document workflows or medical professional recommendation systems.
- RAG or LlamaIndex for the current project stage.

## Safety Boundary

The intended use is educational and research-oriented biomedical QA engineering. Safety boundaries are documented, but no trained model, runtime enforcement, or clinical validation exists.
