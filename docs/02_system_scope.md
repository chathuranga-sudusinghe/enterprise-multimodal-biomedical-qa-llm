# System Scope

The system is planned as an enterprise-ready biomedical QA and medical VQA fine-tuning project using Qwen2.5-Omni.

## In Scope

- PubMedQA text QA.
- SLAKE image-text QA.
- Qwen2.5-Omni fine-tuning planning.
- Prompt-only baselines.
- Supervised fine-tuning.
- Instruction tuning.
- LoRA and QLoRA experiments.
- DPO preference tuning.
- Safety tuning.
- Structured outputs with evidence, answer, uncertainty, and safety fields.
- Evaluation for answer quality, evidence consistency, visual grounding, hallucination checks, safety compliance, JSON validity, latency, and resource usage.
- Future API planning.

## Out of Scope

- Patient-specific diagnosis.
- Treatment advice.
- Prescription advice.
- Replacement for medical professionals.
- Restricted clinical-record datasets.
- Private patient data.
- Hospital record summarization.
- Healthcare document workflow automation.
- Medical professional recommendation workflows.
- RAG or LlamaIndex for version 1.

## Safety Boundary

This project is not a diagnosis system, not a treatment recommendation system, not a replacement for medical professionals, and not a patient-specific decision system. Outputs are educational, research-oriented, evidence-aware health information support.
