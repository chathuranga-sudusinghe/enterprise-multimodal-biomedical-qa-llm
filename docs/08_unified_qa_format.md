# Unified Biomedical QA Record Contract

## 1. Objective

The unified QA record contract/schema provides one stable representation for biomedical text QA and medical image-text QA. It keeps shared fields consistent while preserving dataset-specific provenance, labels, language, and visual metadata.

The tracked schema builders implement one-record transformations and validation. They do not form a completed preprocessing pipeline, create processed datasets, load Qwen2.5-Omni, or implement training.

## 2. Supported Dataset Tracks

- **PubMedQA:** biomedical text QA grounded in supplied research abstract context.
- **SLAKE:** medical image-text QA grounded in a referenced medical image.

PathVQA remains optional future or backup data and is not part of the current preprocessing contract.

## 3. Shared QA Record Schema

Each transformed record uses five top-level fields:

```json
{
  "task_type": "biomedical_text_qa",
  "instruction": "Answer the biomedical research question using only the provided context.",
  "input": {"question": "...", "context": ["..."]},
  "target": {"answer": "...", "label": "yes"},
  "metadata": {"dataset": "PubMedQA", "source_config": "pqa_labeled"}
}
```

- `task_type` distinguishes text QA from image-text QA.
- `instruction` defines a bounded, evidence-aware task.
- `input` contains the question and available evidence.
- `target` contains the expected answer and optional dataset label.
- `metadata` preserves provenance and dataset-specific attributes.

## 4. PubMedQA Example Format

```json
{
  "task_type": "biomedical_text_qa",
  "instruction": "Answer the biomedical research question using only the provided context. State when the evidence is insufficient.",
  "input": {
    "question": "Does the intervention improve the reported outcome?",
    "context": ["Background...", "Results..."]
  },
  "target": {
    "answer": "The study reports an improvement in the measured outcome.",
    "label": "yes"
  },
  "metadata": {
    "dataset": "PubMedQA",
    "source_config": "pqa_labeled",
    "pubid": "12345678",
    "context_text_count": 2
  }
}
```

## 5. SLAKE Example Format

```json
{
  "task_type": "medical_visual_qa",
  "instruction": "Answer the medical image question using only the provided image and question. State when the visual evidence is insufficient.",
  "input": {
    "question": "What modality is shown?",
    "image_path": "data/raw/slake/source_files/imgs/example/source.jpg"
  },
  "target": {"answer": "CT", "label": null},
  "metadata": {
    "dataset": "SLAKE",
    "split_name": "train",
    "answer_type": "OPEN",
    "modality": "CT",
    "location": "Brain",
    "content_type": "Modality",
    "q_lang": "en"
  }
}
```

## 6. Required Fields

Every example requires a non-empty `task_type` and `instruction`, an `input` dictionary with a non-empty `question`, a `target` dictionary with a non-empty `answer`, and a `metadata` dictionary with a non-empty `dataset`.

PubMedQA additionally requires `input.context` and `metadata.source_config`. SLAKE additionally requires `input.image_path` and `metadata.split_name`.

## 7. Optional Metadata Fields

Optional metadata may include `pubid`, `qid`, `img_id`, source configuration, context count, split, image name, answer type, modality, anatomical location, content type, question language, and base type. A future pipeline may add preprocessing version, license reference, filtering reason, and validation status.

Optional values must not be invented. They should be omitted or represented consistently as `null`.

## 8. Safety and Evidence-Grounding Rules

- Ground answers only in the supplied abstract context or image-question pair.
- Do not frame tasks as patient-specific diagnosis, treatment selection, prescription guidance, or replacement for medical professionals.
- State uncertainty when evidence is absent, ambiguous, or insufficient.
- Keep evidence distinguishable from interpretation in future structured targets.
- Treat dataset answers as supervision signals, not verified clinical recommendations.
- Retain source provenance and original split membership.

## 9. Dataset-Specific Policy Decisions

### PubMedQA Configurations

- `pqa_labeled`: primary supervised evaluation and high-confidence instruction-tuning source because it includes expert labels.
- `pqa_artificial`: optional supervised training source. Keep provenance explicit, measure its strong label imbalance, and do not silently mix it with labeled examples.
- `pqa_unlabeled`: exclude from direct supervised classification or instruction-tuning targets because `final_decision` is absent. Reserve it for future explicitly designed unsupervised or weak-supervision work.

### SLAKE Language Handling

- Preserve `q_lang` for every example.
- Keep English and Chinese examples distinguishable during preprocessing and evaluation.
- Do not translate, merge, or discard either language without a documented experiment policy.
- Report results by language as well as overall where practical.

### Missing or Incomplete Records

- Reject records missing fields needed for the selected track's required input or target.
- Record rejection counts and reasons in preprocessing reports.
- Never fabricate missing answers, labels, questions, contexts, or image paths.
- Review the known incomplete SLAKE training record before conversion.

### Image Path Handling

- Store repository-relative image paths, not machine-specific absolute paths.
- Validate that each image exists during preprocessing.
- Preserve the original SLAKE image name in metadata.
- Do not copy images into Git-tracked processed-data folders.

## 10. Planned Preprocessing Implementation

A future engineering step should implement a deterministic conversion pipeline that:

1. Reads each inspected raw dataset configuration or split.
2. Applies explicit inclusion, exclusion, and language policies.
3. Uses the schema builders for one-record transformation.
4. Validates every unified example and records rejection reasons.
5. Preserves original splits and provenance.
6. Writes versioned local outputs under ignored `data/processed/` paths.
7. Produces summary statistics and small safe previews.
8. Tests conversion, filtering, reproducibility, and split integrity.

Prompt templates, tokenization limits, baseline inference, and Qwen2.5-Omni fine-tuning should be addressed only after the processed schema and evaluation contract are reviewed.
