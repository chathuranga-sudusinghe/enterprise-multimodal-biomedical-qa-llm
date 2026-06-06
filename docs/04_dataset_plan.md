## SLAKE raw inspection workflow

The SLAKE dataset should be inspected from the locally downloaded raw files before any preprocessing format is finalized. Use the lightweight inspection command:

```bash
python -m omni_clinical_llm.data.inspect_slake --raw-dir data/raw/slake/source_files --output artifacts/dataset_reports/slake_inspection_report.json
```

The inspection report captures split row counts, detected columns, required-field gaps, missing image files, and distributions for answer type, modality, location, question language, and content type. It also records a few valid image path examples so the raw JSON-to-image linkage can be checked quickly.

Preprocessing schemas and any future fine-tuning format should be finalized only after reviewing these inspection results. This keeps the data pipeline grounded in the actual SLAKE files available locally rather than assumptions about the dataset structure.

## PubMedQA raw inspection workflow

PubMedQA supports the biomedical text QA track for this project. Inspect the locally downloaded raw JSONL files before finalizing any text QA preprocessing or fine-tuning format:

```bash
python -m omni_clinical_llm.data.inspect_pubmedqa --raw-dir data/raw/pubmedqa/source_files --output artifacts/dataset_reports/pubmedqa_inspection_report.json
```

The inspection report captures row counts by PubMedQA config, detected columns, missing required fields, final decision labels, question and answer length statistics, context size statistics, and short safe sample records.

Text QA preprocessing schemas and fine-tuning examples should be finalized only after reviewing the PubMedQA inspection results. SLAKE supports the medical image-text QA track, while PathVQA remains optional backup or future data and is not required now.
