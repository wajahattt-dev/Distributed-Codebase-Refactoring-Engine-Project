# Main Orchestrator Engine

from .router import Router
from .git_manager import GitManager
from .report_generator import ReportGenerator
from ..configs.settings import Settings

class RefactoringEngine:
    def __init__(self, settings_path: str):
        self.settings = Settings.load(settings_path)
        self.router = Router(self.settings)
        self.git_manager = GitManager(self.settings)
        self.report_generator = ReportGenerator(self.settings)

    def run(self, repo_path: str):
        branch = self.git_manager.create_refactor_branch(repo_path)
        results = self.router.dispatch(repo_path)
        self.git_manager.commit_changes(repo_path, branch)
        report_path = self.report_generator.generate(results)
        return report_path
