## SLAKE data inspection

Run the lightweight SLAKE raw data inspection utility after downloading the dataset locally:

```bash
python -m omni_clinical_llm.data.inspect_slake --raw-dir data/raw/slake/source_files --output artifacts/dataset_reports/slake_inspection_report.json
```

The raw SLAKE files under `data/raw/` are ignored by Git and must not be committed. The generated inspection report is intended to guide the next preprocessing and fine-tuning format decisions.
