# Current Project Status

## Status Definitions

- **Implemented:** tracked code or documentation exists.
- **Locally executed:** local generated evidence was observed but is excluded from Git.
- **Publicly evidenced:** tracked repository files demonstrate the capability.
- **Planned:** documented future work without implementation.
- **Not implemented:** no working capability exists in the repository.

## Capability Matrix

| Capability | Status | Evidence path | Execution evidence | Next step |
|---|---|---|---|---|
| PubMedQA inspection | Implemented; locally executed | `src/omni_clinical_llm/data/inspect_pubmedqa.py`, `tests/test_inspect_pubmedqa.py` | Ignored local report observed; not publicly tracked | Confirm source metadata and review report before conversion |
| SLAKE inspection | Implemented; locally executed | `src/omni_clinical_llm/data/inspect_slake.py`, `tests/test_inspect_slake.py` | Ignored local report observed; not publicly tracked | Confirm source metadata and review split/image findings |
| Unified QA schema | Implemented; publicly evidenced | `src/omni_clinical_llm/data/qa_schema.py`, `docs/08_unified_qa_format.md` | Builders and validator are tracked; no processed dataset generated | Approve policies before implementing conversion |
| Tests | Implemented; publicly evidenced | `tests/` | Not executed during the audit or remediation; no current pass claim | Run in a separately approved verification task |
| Deterministic preprocessing | Partially implemented | `src/omni_clinical_llm/data/qa_schema.py` | Deterministic one-record builders exist; no end-to-end pipeline or output evidence | Add versioned conversion, rejection reporting, and split checks |
| Model loading | Not implemented | `configs/model_config.yaml` | Disabled; no model cache or load report is tracked | Pin model revision and implement baseline loader |
| Prompt-only baseline | Planned | `docs/05_baseline_and_evaluation_plan.md` | No inference output or metrics | Implement after model and dataset approvals |
| SFT | Planned | `docs/05_baseline_and_evaluation_plan.md` | No training code, run, or checkpoint | Define reviewed baseline and training configuration first |
| LoRA | Planned | `docs/05_baseline_and_evaluation_plan.md` | No adapter or run evidence | Evaluate only after prompt baseline |
| QLoRA | Planned | `docs/05_baseline_and_evaluation_plan.md` | No adapter or run evidence | Evaluate hardware and quantization requirements |
| DPO | Planned | `docs/05_baseline_and_evaluation_plan.md` | No preference data or training evidence | Define preference-data provenance and safety review |
| Safety tuning | Planned | `docs/05_baseline_and_evaluation_plan.md`, `configs/safety_policy.yaml` | Safety boundaries are documented; tuning is absent | Define measurable safety evaluation before tuning |
| Multimodal training | Planned | `docs/03_architecture.md` | Image-text schema preparation only | Establish image-text baseline and evaluation first |
| Evaluation | Planned | `configs/evaluation_config.yaml` | Disabled; no metrics or comparison reports | Implement metric definitions and evaluation runner |
| API | Not implemented | `docs/02_system_scope.md` | No API module or runtime evidence | Reconsider only after model evaluation exists |
| Docker | Not implemented | `docs/02_system_scope.md` | No container files | Reconsider only when a runnable workload exists |
| CI | Not implemented | Repository root | No workflow files | Add only after local test workflow is stable |

## Current Maturity Boundary

The repository currently provides data inspection, validation, and a unified QA record contract. It does not provide a model, a completed preprocessing pipeline, a fine-tuning system, evaluation results, or a deployable service.
