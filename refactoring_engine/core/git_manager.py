# Commits, branches, diffs

import git
import os
from datetime import datetime

class GitManager:
    def __init__(self, settings):
        self.settings = settings

    def create_refactor_branch(self, repo_path):
        repo = git.Repo(repo_path)
        branch_name = f"refactor/suggested_modularization_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        repo.git.checkout('HEAD', b=branch_name)
        return branch_name

    def commit_changes(self, repo_path, branch_name):
        repo = git.Repo(repo_path)
        repo.git.add(A=True)
        repo.index.commit(f"Refactor: Automated modularization on {branch_name}")
