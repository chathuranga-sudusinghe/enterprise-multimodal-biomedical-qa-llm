# Safety Governance

Biomedical QA and medical VQA require explicit safety boundaries, evidence handling, source review, and clear uncertainty behavior.

## Safety Boundaries

- No diagnosis.
- No treatment decision.
- No patient-specific medical advice.
- No prescription guidance.
- No replacement for medical professionals.

Outputs are educational and research support only.

## Required Model Behavior

- State uncertainty when evidence is insufficient.
- Separate evidence from interpretation.
- Avoid unsupported biomedical or medical-image claims.
- Avoid presenting generated content as definitive medical advice.
- Include safety notes when the question exceeds the supported evidence.

## Governance Notes

- Check dataset licenses before use.
- Use only datasets with access, license, and redistribution terms reviewed by the human project owner.
- Do not use private patient data.
- Keep raw datasets out of Git.
- Track dataset provenance, preprocessing decisions, evaluation methods, and known limitations.
- Review deployment readiness before production use.
