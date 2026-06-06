import json
from pathlib import Path

from omni_clinical_llm.data.inspect_pubmedqa import (
    extract_context_texts,
    inspect_pubmedqa_dataset,
    inspect_pubmedqa_file,
    load_jsonl_records,
    text_length_stats,
    validate_pubmedqa_record,
)


def _write_jsonl(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "\n".join(json.dumps(record) for record in records) + "\n",
        encoding="utf-8",
    )


def _valid_record(pubid: str = "123") -> dict:
    return {
        "pubid": pubid,
        "question": "Does the treatment improve outcomes?",
        "context": {"contexts": ["Background text.", "Methods text."]},
        "long_answer": "The treatment improved outcomes in the study cohort.",
        "final_decision": "yes",
    }


def test_load_jsonl_records_loads_jsonl_records(tmp_path: Path) -> None:
    jsonl_path = tmp_path / "train.jsonl"
    records = [_valid_record("1"), _valid_record("2")]
    _write_jsonl(jsonl_path, records)

    assert load_jsonl_records(jsonl_path) == records


def test_validate_pubmedqa_record_detects_missing_fields() -> None:
    record = _valid_record()
    record["long_answer"] = ""
    record.pop("context")

    validation = validate_pubmedqa_record(record)

    assert validation["is_valid"] is False
    assert validation["missing_required_fields_count"] == 2
    assert validation["missing_fields"] == ["context", "long_answer"]


def test_extract_context_texts_handles_dict_context_with_contexts_list() -> None:
    context = {"contexts": ["first", "second", None, ""]}

    assert extract_context_texts(context) == ["first", "second"]


def test_extract_context_texts_handles_list_context() -> None:
    assert extract_context_texts(["first", 3, "second", ""]) == ["first", "second"]


def test_extract_context_texts_handles_string_context() -> None:
    assert extract_context_texts("single context") == ["single context"]


def test_extract_context_texts_handles_missing_unexpected_context_safely() -> None:
    assert extract_context_texts(None) == []
    assert extract_context_texts({"labels": ["not text"]}) == []
    assert extract_context_texts(7) == []


def test_text_length_stats_returns_correct_min_max_mean_median() -> None:
    assert text_length_stats([1, 2, 6]) == {
        "min": 1,
        "max": 6,
        "mean": 3,
        "median": 2,
    }


def test_text_length_stats_handles_empty_values() -> None:
    assert text_length_stats([]) == {
        "min": 0,
        "max": 0,
        "mean": 0,
        "median": 0,
    }


def test_inspect_pubmedqa_file_counts_rows_correctly(tmp_path: Path) -> None:
    jsonl_path = tmp_path / "pqa_labeled" / "train.jsonl"
    _write_jsonl(jsonl_path, [_valid_record("1"), _valid_record("2")])

    report = inspect_pubmedqa_file(jsonl_path)

    assert report["config_name"] == "pqa_labeled"
    assert report["row_count"] == 2
    assert report["missing_required_fields_count"] == 0
    assert report["sample_records"][0]["context_text_count"] == 2


def test_inspect_pubmedqa_file_counts_missing_fields_correctly(
    tmp_path: Path,
) -> None:
    jsonl_path = tmp_path / "pqa_artificial" / "train.jsonl"
    missing_record = _valid_record("1")
    missing_record["question"] = ""
    missing_record["final_decision"] = None
    _write_jsonl(jsonl_path, [_valid_record("0"), missing_record])

    report = inspect_pubmedqa_file(jsonl_path)

    assert report["missing_required_fields_count"] == 2
    assert report["rows_with_missing_required_fields_count"] == 1


def test_inspect_pubmedqa_file_reports_final_decision_distribution(
    tmp_path: Path,
) -> None:
    jsonl_path = tmp_path / "pqa_unlabeled" / "train.jsonl"
    yes_record = _valid_record("1")
    no_record = _valid_record("2")
    no_record["final_decision"] = "no"
    _write_jsonl(jsonl_path, [yes_record, no_record])

    report = inspect_pubmedqa_file(jsonl_path)

    assert report["final_decision_distribution"] == {"yes": 1, "no": 1}


def test_inspect_pubmedqa_dataset_handles_expected_configs(tmp_path: Path) -> None:
    raw_dir = tmp_path / "source_files"
    _write_jsonl(raw_dir / "pqa_labeled" / "train.jsonl", [_valid_record("1")])
    _write_jsonl(raw_dir / "pqa_artificial" / "train.jsonl", [_valid_record("2")])
    _write_jsonl(raw_dir / "pqa_unlabeled" / "train.jsonl", [_valid_record("3")])

    report = inspect_pubmedqa_dataset(raw_dir)

    assert report["dataset"] == "PubMedQA"
    assert report["config_names"] == [
        "pqa_labeled",
        "pqa_artificial",
        "pqa_unlabeled",
    ]
    assert report["total_row_count"] == 3
    assert report["row_counts_by_config"] == {
        "pqa_labeled": 1,
        "pqa_artificial": 1,
        "pqa_unlabeled": 1,
    }
