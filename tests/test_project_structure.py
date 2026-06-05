from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_required_directories_exist() -> None:
    required_directories = [
        "configs",
        "docs",
        "src/omni_clinical_llm",
        "src/omni_clinical_llm/data",
        "src/omni_clinical_llm/inference",
        "src/omni_clinical_llm/evaluation",
        "src/omni_clinical_llm/training",
        "src/omni_clinical_llm/governance",
        "tests",
        "artifacts",
    ]

    for relative_path in required_directories:
        assert (PROJECT_ROOT / relative_path).is_dir()


def test_required_config_files_exist() -> None:
    required_config_files = [
        "configs/model_config.yaml",
        "configs/dataset_config.yaml",
        "configs/evaluation_config.yaml",
        "configs/safety_policy.yaml",
    ]

    for relative_path in required_config_files:
        assert (PROJECT_ROOT / relative_path).is_file()


def test_required_root_files_exist() -> None:
    required_root_files = [
        "README.md",
        "requirements.txt",
        "pyproject.toml",
        ".env.example",
    ]

    for relative_path in required_root_files:
        assert (PROJECT_ROOT / relative_path).is_file()


def test_old_project_direction_terms_are_absent() -> None:
    scanned_roots = [
        PROJECT_ROOT / "README.md",
        PROJECT_ROOT / "docs",
        PROJECT_ROOT / "configs",
        PROJECT_ROOT / "src",
        PROJECT_ROOT / "tests",
    ]
    excluded_dirs = {".git", ".venv", ".pytest_cache", "__pycache__", "data"}
    blocked_terms = [
        "M" + "IMIC",
        "m" + "imic",
        "Physio" + "Net",
        "CI" + "TI",
        "credential" + "ed",
        "dis" + "charge",
        "hospital " + "course",
        "clinical " + "documentation",
        "doctor " + "support",
        "doctor " + "recommendation",
        "patient " + "record",
        "clinical " + "note",
        "clin" + "ician",
    ]

    files_to_scan = []
    for root in scanned_roots:
        if root.is_file():
            files_to_scan.append(root)
            continue

        for path in root.rglob("*"):
            if not path.is_file():
                continue
            if any(part in excluded_dirs for part in path.parts):
                continue
            files_to_scan.append(path)

    violations = []
    for path in files_to_scan:
        text = path.read_text(encoding="utf-8")
        lower_text = text.lower()
        for term in blocked_terms:
            if term.lower() in lower_text:
                violations.append(f"{path.relative_to(PROJECT_ROOT)}: {term}")

    assert not violations, "Old project references remain:\n" + "\n".join(violations)
