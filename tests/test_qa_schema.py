from omni_clinical_llm.data.qa_schema import (
    build_pubmedqa_example,
    build_slake_example,
    validate_unified_qa_example,
)

UNSAFE_CLINICAL_PHRASES = (
    "diagnose the patient",
    "recommend treatment",
    "prescribe medication",
)


def test_pubmedqa_example_contains_shared_sections() -> None:
    record = {
        "pubid": "123",
        "question": "Does the intervention improve outcomes?",
        "context": {"contexts": ["Background.", "Results."]},
        "long_answer": "The study reports improved outcomes.",
        "final_decision": "yes",
    }

    example = build_pubmedqa_example(record, "pqa_labeled")

    assert example["task_type"] == "biomedical_text_qa"
    assert example["instruction"]
    assert example["input"]["context"] == ["Background.", "Results."]
    assert example["target"]["label"] == "yes"
    assert example["metadata"]["dataset"] == "PubMedQA"
    assert example["metadata"]["source_config"] == "pqa_labeled"


def test_slake_example_contains_image_path_and_visual_metadata() -> None:
    record = {
        "qid": 10,
        "img_id": 20,
        "img_name": "xmlab1/source.jpg",
        "question": "What modality is shown?",
        "answer": "CT",
        "answer_type": "OPEN",
        "modality": "CT",
        "location": "Brain",
        "content_type": "Modality",
        "q_lang": "en",
        "base_type": "vqa",
    }

    example = build_slake_example(
        record,
        "data/raw/slake/source_files/imgs/xmlab1/source.jpg",
        "train",
    )

    assert example["task_type"] == "medical_visual_qa"
    assert example["input"]["image_path"].endswith("xmlab1/source.jpg")
    assert example["metadata"]["dataset"] == "SLAKE"
    assert example["metadata"]["split_name"] == "train"
    assert example["metadata"]["modality"] == "CT"
    assert example["metadata"]["q_lang"] == "en"


def test_validator_detects_missing_top_level_fields() -> None:
    validation = validate_unified_qa_example(
        {
            "task_type": "biomedical_text_qa",
            "input": {"question": "Question?", "context": []},
        }
    )

    assert validation["is_valid"] is False
    assert validation["missing_fields"] == [
        "instruction",
        "target",
        "metadata",
    ]


def test_generated_examples_avoid_unsafe_clinical_wording() -> None:
    pubmedqa_example = build_pubmedqa_example(
        {
            "pubid": "123",
            "question": "Does the study report an association?",
            "context": ["Study context."],
            "long_answer": "An association was reported.",
            "final_decision": "yes",
        },
        "pqa_labeled",
    )
    slake_example = build_slake_example(
        {
            "question": "Which organ is visible?",
            "answer": "Lung",
            "img_name": "image.jpg",
            "q_lang": "en",
        },
        "data/raw/slake/source_files/imgs/image.jpg",
        "train",
    )

    instructions = (
        pubmedqa_example["instruction"].lower(),
        slake_example["instruction"].lower(),
    )
    for instruction in instructions:
        assert all(phrase not in instruction for phrase in UNSAFE_CLINICAL_PHRASES)


def test_built_examples_pass_validation() -> None:
    pubmedqa_example = build_pubmedqa_example(
        {
            "pubid": "123",
            "question": "Is the result statistically significant?",
            "context": "Study result context.",
            "long_answer": "The result was statistically significant.",
            "final_decision": "yes",
        },
        "pqa_labeled",
    )
    slake_example = build_slake_example(
        {
            "question": "What modality is shown?",
            "answer": "MRI",
            "img_name": "image.jpg",
        },
        "data/raw/slake/source_files/imgs/image.jpg",
        "validation",
    )

    assert validate_unified_qa_example(pubmedqa_example)["is_valid"] is True
    assert validate_unified_qa_example(slake_example)["is_valid"] is True
