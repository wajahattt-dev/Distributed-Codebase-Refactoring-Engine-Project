# Unit tests for orchestration
import pytest
from refactoring_engine.core.engine import RefactoringEngine

def test_engine_runs(tmp_path):
    # Setup: create a dummy repo
    repo_path = tmp_path / "repo"
    repo_path.mkdir()
    (repo_path / "foo.py").write_text("def foo():\n    return 42\n")
    engine = RefactoringEngine('configs/settings.yaml')
    report_path = engine.run(str(repo_path))
    assert report_path.endswith('.md')
