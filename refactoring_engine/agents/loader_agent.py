# Loads + chunks monolithic code

from .base import BaseAgent
from ..utils.file_loader import load_python_files

class LoaderAgent(BaseAgent):
    def run(self, repo_path):
        files = load_python_files(repo_path)
        # Optionally chunk large files here
        return files
