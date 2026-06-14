# Dataset Plan

## Current Dataset Roles

- PubMedQA supports biomedical text QA.
- SLAKE supports medical image-text QA.
- PathVQA is optional future scope and is not part of the current unified QA record contract.

Dataset access and redistribution terms require human review. The repository does not claim that any dataset is freely available.

## Implemented Inspection Workflow

```bash
python -m omni_clinical_llm.data.inspect_pubmedqa --raw-dir data/raw/pubmedqa/source_files --output artifacts/dataset_reports/pubmedqa_inspection_report.json

python -m omni_clinical_llm.data.inspect_slake --raw-dir data/raw/slake/source_files --output artifacts/dataset_reports/slake_inspection_report.json
```

The PubMedQA inspector covers `pqa_labeled`, `pqa_artificial`, and `pqa_unlabeled`. The SLAKE inspector covers train, validation, and test splits plus referenced image existence. Generated reports and raw files remain local and ignored by Git.

## Implemented Schema Stage

`docs/08_unified_qa_format.md` defines the shared record contract, and `src/omni_clinical_llm/data/qa_schema.py` implements one-record builders and validation. This is not a completed preprocessing pipeline.

## Planned Deterministic Preprocessing

The next data implementation should:

1. Verify dataset source, version, license, access date, and checksums.
2. Apply reviewed inclusion, exclusion, language, and image-path policies.
3. Preserve original splits and provenance.
4. Record rejection reasons and summary statistics.
5. Write versioned outputs only under ignored local paths.
6. Add reproducibility and split-integrity tests without committing raw examples.
