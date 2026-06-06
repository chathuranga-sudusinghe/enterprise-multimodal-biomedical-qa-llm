## SLAKE raw inspection workflow

The SLAKE dataset should be inspected from the locally downloaded raw files before any preprocessing format is finalized. Use the lightweight inspection command:

```bash
python -m omni_clinical_llm.data.inspect_slake --raw-dir data/raw/slake/source_files --output artifacts/dataset_reports/slake_inspection_report.json
```

The inspection report captures split row counts, detected columns, required-field gaps, missing image files, and distributions for answer type, modality, location, question language, and content type. It also records a few valid image path examples so the raw JSON-to-image linkage can be checked quickly.

Preprocessing schemas and any future fine-tuning format should be finalized only after reviewing these inspection results. This keeps the data pipeline grounded in the actual SLAKE files available locally rather than assumptions about the dataset structure.
