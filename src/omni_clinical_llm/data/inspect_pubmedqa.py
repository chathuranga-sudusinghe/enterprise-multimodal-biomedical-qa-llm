"""Lightweight inspection utilities for the raw PubMedQA dataset."""

from __future__ import annotations

import argparse
import json
import logging
import statistics
from collections import Counter
from pathlib import Path

LOGGER = logging.getLogger(__name__)

REQUIRED_FIELDS = (
    "pubid",
    "question",
    "context",
    "long_answer",
    "final_decision",
)

CONFIG_FILES = {
    "pqa_labeled": Path("pqa_labeled") / "train.jsonl",
    "pqa_artificial": Path("pqa_artificial") / "train.jsonl",
    "pqa_unlabeled": Path("pqa_unlabeled") / "train.jsonl",
}

LONG_ANSWER_PREVIEW_CHARS = 240


def load_jsonl_records(path: Path) -> list[dict]:
    """Load JSONL records from a file containing one JSON object per line."""
    LOGGER.info("Loading PubMedQA JSONL records from %s", path)
    records: list[dict] = []

    with path.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            stripped_line = line.strip()
            if not stripped_line:
                continue

            record = json.loads(stripped_line)
            if not isinstance(record, dict):
                raise ValueError(
                    f"Expected JSON object at {path}:{line_number}, "
                    f"got {type(record).__name__}"
                )
            records.append(record)

    return records


def validate_pubmedqa_record(record: dict) -> dict:
    """Return validation metadata for one raw PubMedQA record."""
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


def extract_context_texts(context: object) -> list[str]:
    """Extract clean context strings from common PubMedQA context structures."""
    if isinstance(context, str):
        return [context] if context else []

    if isinstance(context, list):
        return [item for item in context if isinstance(item, str) and item]

    if isinstance(context, dict):
        contexts = context.get("contexts")
        if isinstance(contexts, list):
            return [item for item in contexts if isinstance(item, str) and item]
        if isinstance(contexts, str) and contexts:
            return [contexts]

    return []


def text_length_stats(values: list[int]) -> dict:
    """Return min, max, mean, and median for text length values."""
    if not values:
        return {
            "min": 0,
            "max": 0,
            "mean": 0,
            "median": 0,
        }

    return {
        "min": min(values),
        "max": max(values),
        "mean": statistics.mean(values),
        "median": statistics.median(values),
    }


def inspect_pubmedqa_file(jsonl_path: Path) -> dict:
    """Inspect one PubMedQA JSONL file and return summary statistics."""
    records = load_jsonl_records(jsonl_path)
    detected_columns = sorted({key for record in records for key in record})
    final_decision_counter: Counter = Counter()
    missing_required_fields_count = 0
    rows_with_missing_required_fields_count = 0
    question_lengths: list[int] = []
    long_answer_lengths: list[int] = []
    context_item_counts: list[int] = []
    context_text_lengths: list[int] = []
    sample_records: list[dict] = []

    for record in records:
        validation = validate_pubmedqa_record(record)
        missing_count = validation["missing_required_fields_count"]
        missing_required_fields_count += missing_count
        if missing_count:
            rows_with_missing_required_fields_count += 1

        final_decision = record.get("final_decision")
        if final_decision not in (None, ""):
            final_decision_counter[str(final_decision)] += 1

        question = record.get("question")
        if isinstance(question, str):
            question_lengths.append(len(question))

        long_answer = record.get("long_answer")
        if isinstance(long_answer, str):
            long_answer_lengths.append(len(long_answer))

        context_texts = extract_context_texts(record.get("context"))
        context_item_counts.append(len(context_texts))
        context_text_lengths.extend(len(text) for text in context_texts)

        if len(sample_records) < 3:
            long_answer_preview = long_answer if isinstance(long_answer, str) else ""
            sample_records.append(
                {
                    "pubid": record.get("pubid"),
                    "question": question if isinstance(question, str) else "",
                    "final_decision": final_decision,
                    "long_answer_preview": long_answer_preview[
                        :LONG_ANSWER_PREVIEW_CHARS
                    ],
                    "context_text_count": len(context_texts),
                }
            )

    return {
        "config_name": jsonl_path.parent.name,
        "jsonl_path": str(jsonl_path),
        "row_count": len(records),
        "detected_columns": detected_columns,
        "missing_required_fields_count": missing_required_fields_count,
        "rows_with_missing_required_fields_count": (
            rows_with_missing_required_fields_count
        ),
        "final_decision_distribution": dict(final_decision_counter),
        "question_length_statistics": text_length_stats(question_lengths),
        "long_answer_length_statistics": text_length_stats(long_answer_lengths),
        "context_item_count_statistics": text_length_stats(context_item_counts),
        "context_text_length_statistics": text_length_stats(context_text_lengths),
        "sample_records": sample_records,
    }


def inspect_pubmedqa_dataset(raw_dir: Path) -> dict:
    """Inspect the expected PubMedQA raw JSONL files."""
    configs = {
        config_name: inspect_pubmedqa_file(raw_dir / relative_path)
        for config_name, relative_path in CONFIG_FILES.items()
    }
    row_counts_by_config = {
        config_name: config_report["row_count"]
        for config_name, config_report in configs.items()
    }

    return {
        "dataset": "PubMedQA",
        "raw_dir": str(raw_dir),
        "config_names": list(CONFIG_FILES.keys()),
        "total_row_count": sum(row_counts_by_config.values()),
        "row_counts_by_config": row_counts_by_config,
        "files_inspected": [
            str(raw_dir / relative_path) for relative_path in CONFIG_FILES.values()
        ],
        "configs": configs,
    }


def write_report(report: dict, output_path: Path) -> None:
    """Write a JSON inspection report, creating the output folder if needed."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    LOGGER.info("Writing PubMedQA inspection report to %s", output_path)
    with output_path.open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=2, sort_keys=True)
        file.write("\n")


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Inspect locally downloaded raw PubMedQA JSONL files."
    )
    parser.add_argument(
        "--raw-dir",
        type=Path,
        required=True,
        help="Directory containing pqa_labeled, pqa_artificial, and pqa_unlabeled.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help="Path where the JSON inspection report should be written.",
    )
    return parser


def main() -> None:
    """Run the PubMedQA inspection CLI."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")
    parser = _build_parser()
    args = parser.parse_args()

    report = inspect_pubmedqa_dataset(args.raw_dir)
    write_report(report, args.output)


if __name__ == "__main__":
    main()
