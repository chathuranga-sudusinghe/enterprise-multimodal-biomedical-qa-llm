"""Lightweight inspection utilities for the raw SLAKE dataset."""

from __future__ import annotations

import argparse
import json
import logging
from collections import Counter
from pathlib import Path

LOGGER = logging.getLogger(__name__)

REQUIRED_FIELDS = (
    "img_name",
    "question",
    "answer",
    "answer_type",
    "modality",
    "location",
    "content_type",
    "q_lang",
)

DISTRIBUTION_FIELDS = (
    "answer_type",
    "modality",
    "location",
    "q_lang",
    "content_type",
)

SPLIT_FILES = {
    "train": "train.json",
    "validation": "validation.json",
    "test": "test.json",
}


def load_json_records(path: Path) -> list[dict]:
    """Load a JSON file expected to contain a list of object records."""
    LOGGER.info("Loading SLAKE JSON records from %s", path)
    with path.open("r", encoding="utf-8") as file:
        records = json.load(file)

    if not isinstance(records, list):
        raise ValueError(f"Expected a JSON list in {path}")

    if any(not isinstance(record, dict) for record in records):
        raise ValueError(f"Expected all records in {path} to be JSON objects")

    return records


def validate_slake_record(record: dict) -> dict:
    """Return validation metadata for one raw SLAKE record."""
    missing_fields = [
        field
        for field in REQUIRED_FIELDS
        if field not in record or record[field] in (None, "")
    ]
    return {
        "is_valid": not missing_fields,
        "missing_fields": missing_fields,
        "missing_required_fields_count": len(missing_fields),
    }


def resolve_image_path(image_root: Path, img_name: str) -> Path:
    """Build the expected image path for a SLAKE image name."""
    return image_root / img_name


def inspect_split(json_path: Path, image_root: Path) -> dict:
    """Inspect one raw SLAKE JSON split and return summary statistics."""
    records = load_json_records(json_path)
    detected_columns = sorted({key for record in records for key in record})
    distribution_counters = {field: Counter() for field in DISTRIBUTION_FIELDS}
    missing_required_fields_count = 0
    missing_image_file_count = 0
    valid_sample_image_paths: list[str] = []

    for record in records:
        validation = validate_slake_record(record)
        missing_required_fields_count += validation["missing_required_fields_count"]

        for field, counter in distribution_counters.items():
            value = record.get(field)
            if value not in (None, ""):
                counter[str(value)] += 1

        img_name = record.get("img_name")
        if img_name in (None, ""):
            continue

        image_path = resolve_image_path(image_root, str(img_name))
        if image_path.exists():
            if validation["is_valid"] and len(valid_sample_image_paths) < 5:
                valid_sample_image_paths.append(str(image_path))
        else:
            missing_image_file_count += 1

    return {
        "split_name": json_path.stem,
        "json_path": str(json_path),
        "row_count": len(records),
        "detected_columns": detected_columns,
        "missing_required_fields_count": missing_required_fields_count,
        "missing_image_file_count": missing_image_file_count,
        "answer_type_distribution": dict(distribution_counters["answer_type"]),
        "modality_distribution": dict(distribution_counters["modality"]),
        "location_distribution": dict(distribution_counters["location"]),
        "q_lang_distribution": dict(distribution_counters["q_lang"]),
        "content_type_distribution": dict(distribution_counters["content_type"]),
        "valid_sample_image_paths": valid_sample_image_paths,
    }


def inspect_slake_dataset(raw_dir: Path) -> dict:
    """Inspect the expected train, validation, and test SLAKE raw files."""
    image_root = raw_dir / "imgs"
    splits = {
        split_name: inspect_split(raw_dir / file_name, image_root)
        for split_name, file_name in SPLIT_FILES.items()
    }

    return {
        "dataset": "SLAKE",
        "raw_dir": str(raw_dir),
        "image_root": str(image_root),
        "split_names": list(SPLIT_FILES.keys()),
        "row_counts": {
            split_name: split_report["row_count"]
            for split_name, split_report in splits.items()
        },
        "splits": splits,
    }


def write_report(report: dict, output_path: Path) -> None:
    """Write a JSON inspection report, creating the output folder if needed."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    LOGGER.info("Writing SLAKE inspection report to %s", output_path)
    with output_path.open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=2, sort_keys=True)
        file.write("\n")


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Inspect locally downloaded raw SLAKE dataset files."
    )
    parser.add_argument(
        "--raw-dir",
        type=Path,
        required=True,
        help="Directory containing train.json, validation.json, test.json, and imgs/.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help="Path where the JSON inspection report should be written.",
    )
    return parser


def main() -> None:
    """Run the SLAKE inspection CLI."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")
    parser = _build_parser()
    args = parser.parse_args()

    report = inspect_slake_dataset(args.raw_dir)
    write_report(report, args.output)


if __name__ == "__main__":
    main()
