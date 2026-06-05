# Enterprise Multimodal Biomedical QA LLM | Fine-Tuned Qwen2.5-Omni for Biomedical Text QA, Medical Visual Question Answering, and Safe Evidence-Aware Health Information Support

This repository contains the foundation for a research-grade and enterprise-ready fine-tuning project using Qwen2.5-Omni as the primary model direction.

## Problem Addressed

Biomedical evidence and medical images can be difficult to interpret safely. Generic LLMs may answer without grounding, overstate confidence, or produce unsupported claims when asked biomedical and medical-image questions.

This project focuses on fine-tuning Qwen2.5-Omni for safe text and image biomedical question answering. The intended output style is evidence-aware, uncertainty-aware, and bounded to educational and research-oriented health information support.

## System Overview

The planned system has two primary data tracks:

- Text QA path: PubMedQA biomedical research question plus PubMed abstract context to yes, no, or maybe answer with an evidence-aware explanation and uncertainty or safety note.
- Image-text QA path: SLAKE medical image plus question to answer with a visual or evidence explanation and uncertainty or safety note.

The project will use freely available datasets only. Dataset files, model weights, training code, RAG, LlamaIndex, Docker, and heavy infrastructure are intentionally excluded from this foundation step.

## Safety Boundary

This project is not a diagnosis system, not a treatment recommendation system, not a replacement for medical professionals, and not a patient-specific decision system. It provides educational, research-oriented, and evidence-aware biomedical or medical-image QA outputs with uncertainty and safety notes.

The model must state uncertainty when evidence is insufficient, separate evidence from interpretation, and avoid prescription guidance or patient-specific medical advice.

## Planned Fine-Tuning Path

Fine-tuning work will be added in controlled stages after raw dataset inspection:

1. Prompt-only baseline using base Qwen2.5-Omni.
2. Supervised fine-tuning for biomedical text QA.
3. Instruction tuning for structured evidence-aware responses.
4. LoRA experiments for efficient adaptation.
5. QLoRA experiments for lower-memory experimentation.
6. DPO preference tuning for preferred answer style and safety behavior.
7. Safety tuning for refusals, uncertainty, and evidence boundaries.
8. Later multimodal extension evaluation for image-text QA.

No baseline design, preprocessing format, or training format is finalized before real raw data is downloaded and inspected.

## Planned Datasets

Primary datasets:

- PubMedQA for biomedical text question answering.
- SLAKE for medical visual question answering.

Backup or future datasets:

- PathVQA as an additional image-text VQA option.
- Public video or audio datasets only later if freely available, useful, and aligned with the project.

Raw datasets are not committed to Git.

## Local + Cloud Strategy

Local development will focus on documentation, configuration, tests, raw data inspection notes, prompt baselines, and small CPU-friendly utilities. Local experiments may use small subsets only after real dataset inspection.

Cloud GPU work is planned for later fine-tuning and evaluation runs, especially LoRA, QLoRA, DPO, safety tuning, and multimodal experiments. Cloud use should include dataset license review, access control, reproducible experiment tracking, and cost-aware GPU selection.

## Environment Setup

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Linux or macOS:

```bash
source .venv/bin/activate
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
pytest
```
