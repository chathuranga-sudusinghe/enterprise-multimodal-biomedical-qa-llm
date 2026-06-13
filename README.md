## SLAKE data inspection

Run the lightweight SLAKE raw data inspection utility after downloading the dataset locally:

```bash
python -m omni_clinical_llm.data.inspect_slake --raw-dir data/raw/slake/source_files --output artifacts/dataset_reports/slake_inspection_report.json
```

The raw SLAKE files under `data/raw/` are ignored by Git and must not be committed. The generated inspection report is intended to guide the next preprocessing and fine-tuning format decisions.

## PubMedQA data inspection

Run the lightweight PubMedQA raw data inspection utility after downloading the dataset locally:

```bash
python -m omni_clinical_llm.data.inspect_pubmedqa --raw-dir data/raw/pubmedqa/source_files --output artifacts/dataset_reports/pubmedqa_inspection_report.json
```

Raw data under `data/raw/` is ignored by Git and must not be committed. Generated reports under `artifacts/` are local generated outputs and should not be committed.

## Unified QA format

PubMedQA text QA and SLAKE image-text QA use a shared instruction-tuning example contract with `task_type`, `instruction`, `input`, `target`, and `metadata` sections. Dataset-specific evidence inputs, labels, language, visual attributes, and provenance remain explicit. See `docs/08_unified_qa_format.md` for the format and preprocessing policies.
