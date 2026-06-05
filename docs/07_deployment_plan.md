# Deployment Plan

Deployment is planning-only during this repository phase. No Docker files, deployment manifests, model serving code, or cloud automation are included yet.

## Planned Direction

- Begin with local development, dataset inspection notes, prompt baselines, configuration, and tests.
- Add cloud GPU workflows only after dataset licenses, baselines, evaluation plans, and safety boundaries are reviewed.
- Keep model hosting and fine-tuning infrastructure separate from this foundation.
- Use access controls, audit logging, monitoring, and reproducible experiment tracking for future enterprise use.

## Future Endpoints

- `/text-biomedical-qa`
- `/image-medical-vqa`
- `/multimodal-health-qa`
- `/safety-check`

## Current Status

Deployment is not implemented. Future API work should follow the validated biomedical QA and medical VQA evaluation plan.
