# Data Card

## Scope

This document records only dataset information verified from repository code and ignored local inspection reports. It does not assert redistribution rights or complete upstream metadata.

## Dataset Roles

| Dataset | Project role | Locally inspected categories or splits | Local execution evidence |
|---|---|---|---|
| PubMedQA | Biomedical text QA using research questions, supplied abstract context, long answers, and yes/no/maybe-style decisions where available | `pqa_labeled`, `pqa_artificial`, `pqa_unlabeled` | Ignored local report records 273,518 rows across the three configurations |
| SLAKE | Medical image-text QA using image references, questions, answers, language, modality, location, and content metadata | `train`, `validation`, `test` | Ignored local report records 9,835 train, 2,099 validation, and 2,094 test rows |

The datasets are locally available in ignored paths for the current workspace. They are not included in Git, and the local reports are not public evidence.

## Preserved Schema and Provenance Fields

The unified QA record contract preserves:

- Shared fields: `task_type`, `instruction`, `input`, `target`, and `metadata`.
- PubMedQA provenance: dataset name, source configuration, PubMed identifier, and context count.
- SLAKE provenance: dataset name, source split, question and image identifiers, original image name, answer type, modality, anatomical location, content type, question language, and base type where present.
- Repository-relative image paths rather than machine-specific absolute paths.

## Publication and Redistribution

Before publishing raw records, samples, images, processed records, or reports, the human project owner must verify the applicable dataset terms. Repository licensing does not grant rights to redistribute dataset content.

## Metadata Requiring Human Confirmation

### PubMedQA

- Exact source URL: `TBD - human confirmation required`
- Dataset version or revision: `TBD - human confirmation required`
- Access date: `TBD - human confirmation required`
- File checksums: `TBD - human confirmation required`
- License and redistribution terms: `TBD - human confirmation required`

### SLAKE

- Exact source URL: `TBD - human confirmation required`
- Dataset version or revision: `TBD - human confirmation required`
- Access date: `TBD - human confirmation required`
- File checksums: `TBD - human confirmation required`
- License and redistribution terms: `TBD - human confirmation required`
