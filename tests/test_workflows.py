"""Unit tests for GitHub Actions workflow configurations.

Validates: Requirements 2.1, 2.2
"""

import pathlib

import yaml


def _load_workflow(project_root: pathlib.Path, filename: str) -> dict:
    """Load and parse a GitHub Actions workflow YAML file."""
    workflow_path = project_root / ".github" / "workflows" / filename
    with open(workflow_path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def test_ci_pull_request_trigger(project_root: pathlib.Path) -> None:
    """ci.ymlがpull_requestトリガーを持つこと (要件 2.2)."""
    config = _load_workflow(project_root, "ci.yml")
    assert "pull_request" in config["on"], (
        "ci.yml に pull_request トリガーが設定されていません"
    )


def test_deploy_push_trigger(project_root: pathlib.Path) -> None:
    """deploy.ymlがpush（mainブランチ）トリガーを持つこと (要件 2.1)."""
    config = _load_workflow(project_root, "deploy.yml")
    assert "push" in config["on"], (
        "deploy.yml に push トリガーが設定されていません"
    )
    branches = config["on"]["push"].get("branches", [])
    assert "main" in branches, (
        "deploy.yml の push トリガーに main ブランチが含まれていません"
    )


def test_deploy_pages_write_permission(project_root: pathlib.Path) -> None:
    """deploy.ymlにpages: writeパーミッションが設定されていること (要件 2.1)."""
    config = _load_workflow(project_root, "deploy.yml")
    permissions = config.get("permissions", {})
    assert permissions.get("pages") == "write", (
        "deploy.yml に pages: write パーミッションが設定されていません"
    )
