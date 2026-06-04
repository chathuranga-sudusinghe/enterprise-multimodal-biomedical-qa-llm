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
