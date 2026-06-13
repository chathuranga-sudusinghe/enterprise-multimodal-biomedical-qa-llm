"""Shared schema builders for biomedical text QA and medical visual QA."""

from __future__ import annotations

REQUIRED_TOP_LEVEL_FIELDS = (
    "task_type",
    "instruction",
    "input",
    "target",
    "metadata",
)

PUBMEDQA_INSTRUCTION = (
    "Answer the biomedical research question using only the provided context. "
    "State when the evidence is insufficient."
)

SLAKE_INSTRUCTION = (
    "Answer the medical image question using only the provided image and "
    "question. State when the visual evidence is insufficient."
)


def _extract_context_texts(context: object) -> list[str]:
    """Return context strings from common PubMedQA context structures."""
    if isinstance(context, str):
        return [context] if context else []

    if isinstance(context, list):
        return [item for item in context if isinstance(item, str) and item]

    if isinstance(context, dict):
        contexts = context.get("contexts")
        if isinstance(contexts, str):
            return [contexts] if contexts else []
        if isinstance(contexts, list):
            return [item for item in contexts if isinstance(item, str) and item]

    return []


def build_pubmedqa_example(record: dict, source_config: str) -> dict:
    """Transform one already-loaded PubMedQA record into the shared format."""
    context_texts = _extract_context_texts(record.get("context"))

    return {
        "task_type": "biomedical_text_qa",
        "instruction": PUBMEDQA_INSTRUCTION,
        "input": {
            "question": record.get("question"),
            "context": context_texts,
        },
        "target": {
            "answer": record.get("long_answer"),
            "label": record.get("final_decision"),
        },
        "metadata": {
            "dataset": "PubMedQA",
            "source_config": source_config,
            "pubid": record.get("pubid"),
            "context_text_count": len(context_texts),
        },
    }


def build_slake_example(record: dict, image_path: str, split_name: str) -> dict:
    """Transform one already-loaded SLAKE record into the shared format."""
    return {
        "task_type": "medical_visual_qa",
        "instruction": SLAKE_INSTRUCTION,
        "input": {
            "question": record.get("question"),
            "image_path": image_path,
        },
        "target": {
            "answer": record.get("answer"),
            "label": None,
        },
        "metadata": {
            "dataset": "SLAKE",
            "split_name": split_name,
            "qid": record.get("qid"),
            "img_id": record.get("img_id"),
            "img_name": record.get("img_name"),
            "answer_type": record.get("answer_type"),
            "modality": record.get("modality"),
            "location": record.get("location"),
            "content_type": record.get("content_type"),
            "q_lang": record.get("q_lang"),
            "base_type": record.get("base_type"),
        },
    }


def validate_unified_qa_example(example: dict) -> dict:
    """Validate the shared top-level contract and core nested fields."""
    missing_fields = [
        field
        for field in REQUIRED_TOP_LEVEL_FIELDS
        if field not in example or example[field] in (None, "")
    ]
    invalid_fields: list[str] = []

    input_data = example.get("input")
    if "input" not in missing_fields:
        if not isinstance(input_data, dict):
            invalid_fields.append("input")
        elif input_data.get("question") in (None, ""):
            invalid_fields.append("input.question")

    target = example.get("target")
    if "target" not in missing_fields:
        if not isinstance(target, dict):
            invalid_fields.append("target")
        elif "answer" not in target or target["answer"] in (None, ""):
            invalid_fields.append("target.answer")

    metadata = example.get("metadata")
    if "metadata" not in missing_fields:
        if not isinstance(metadata, dict):
            invalid_fields.append("metadata")
        elif metadata.get("dataset") in (None, ""):
            invalid_fields.append("metadata.dataset")

    task_type = example.get("task_type")
    if task_type == "biomedical_text_qa" and isinstance(input_data, dict):
        if not isinstance(input_data.get("context"), list):
            invalid_fields.append("input.context")
    elif task_type == "medical_visual_qa" and isinstance(input_data, dict):
        if input_data.get("image_path") in (None, ""):
            invalid_fields.append("input.image_path")

    errors = [
        *(f"Missing required field: {field}" for field in missing_fields),
        *(f"Invalid required field: {field}" for field in invalid_fields),
    ]
    return {
        "is_valid": not errors,
        "missing_fields": missing_fields,
        "invalid_fields": invalid_fields,
        "errors": errors,
    }
