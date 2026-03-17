"""Common test fixtures for HPC infrastructure documentation site tests."""

import pathlib

import pytest
import yaml


@pytest.fixture(scope="session")
def project_root() -> pathlib.Path:
    """Return the project root directory path."""
    return pathlib.Path(__file__).resolve().parent.parent


@pytest.fixture(scope="session")
def docs_dir(project_root: pathlib.Path) -> pathlib.Path:
    """Return the docs/ directory path."""
    return project_root / "docs"


@pytest.fixture(scope="session")
def mkdocs_config(project_root: pathlib.Path) -> dict:
    """Load and parse mkdocs.yml, returning the configuration as a dict."""
    mkdocs_path = project_root / "mkdocs.yml"
    with open(mkdocs_path, encoding="utf-8") as f:
        return yaml.safe_load(f)
