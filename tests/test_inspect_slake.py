import json
from pathlib import Path

from omni_clinical_llm.data.inspect_slake import (
    inspect_split,
    load_json_records,
    resolve_image_path,
    validate_slake_record,
)


def _write_json(path: Path, records: list[dict]) -> None:
    path.write_text(json.dumps(records), encoding="utf-8")


def _valid_record(img_name: str = "image_001.jpg") -> dict:
    return {
        "img_name": img_name,
        "question": "What finding is visible?",
        "answer": "A lesion",
        "answer_type": "OPEN",
        "modality": "CT",
        "location": "Brain",
        "content_type": "Abnormality",
        "q_lang": "en",
    }


def test_load_json_records_loads_json_list(tmp_path: Path) -> None:
    json_path = tmp_path / "train.json"
    records = [_valid_record()]
    _write_json(json_path, records)

    assert load_json_records(json_path) == records


def test_validate_slake_record_detects_missing_fields() -> None:
    record = _valid_record()
    record["answer"] = ""
    record.pop("modality")

    validation = validate_slake_record(record)

    assert validation["is_valid"] is False
    assert validation["missing_required_fields_count"] == 2
    assert validation["missing_fields"] == ["answer", "modality"]


def test_resolve_image_path_builds_correct_path(tmp_path: Path) -> None:
    image_root = tmp_path / "imgs"

    assert resolve_image_path(image_root, "image_001.jpg") == image_root / "image_001.jpg"


def test_inspect_split_counts_rows_correctly(tmp_path: Path) -> None:
    image_root = tmp_path / "imgs"
    image_root.mkdir()
    (image_root / "image_001.jpg").write_bytes(b"fake-image")
    json_path = tmp_path / "train.json"
    _write_json(json_path, [_valid_record()])

    report = inspect_split(json_path, image_root)

    assert report["split_name"] == "train"
    assert report["row_count"] == 1
    assert report["missing_required_fields_count"] == 0
    assert report["answer_type_distribution"] == {"OPEN": 1}


def test_inspect_split_counts_missing_images(tmp_path: Path) -> None:
    image_root = tmp_path / "imgs"
    image_root.mkdir()
    json_path = tmp_path / "validation.json"
    _write_json(json_path, [_valid_record("missing.jpg")])

    report = inspect_split(json_path, image_root)

    assert report["missing_image_file_count"] == 1
    assert report["valid_sample_image_paths"] == []


def test_inspect_split_includes_valid_sample_image_paths(tmp_path: Path) -> None:
    image_root = tmp_path / "imgs"
    image_root.mkdir()
    image_path = image_root / "image_001.jpg"
    image_path.write_bytes(b"fake-image")
    json_path = tmp_path / "test.json"
    _write_json(json_path, [_valid_record(image_path.name)])

    report = inspect_split(json_path, image_root)

    assert report["missing_image_file_count"] == 0
    assert report["valid_sample_image_paths"] == [str(image_path)]
