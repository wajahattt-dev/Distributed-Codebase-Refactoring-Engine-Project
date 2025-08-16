# FastAPI server (optional GUI/microservice)

from fastapi import FastAPI
from .schemas import RefactorRequest, RefactorResponse
from ..core.engine import RefactoringEngine
import os
import tempfile
import shutil
import git

app = FastAPI()
engine = None

@app.on_event("startup")
def startup_event():
    global engine
    engine = RefactoringEngine('refactoring_engine/configs/settings.yaml')

def is_url(path):
    return path.startswith('http://') or path.startswith('https://')

@app.post("/refactor", response_model=RefactorResponse)
def refactor(request: RefactorRequest):
    repo_path = request.repo_path
    temp_dir = None
    if is_url(repo_path):
        temp_dir = tempfile.mkdtemp(prefix="refactor_repo_")
        try:
            git.Repo.clone_from(repo_path, temp_dir)
            repo_path = temp_dir
        except Exception as e:
            if temp_dir and os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)
            return RefactorResponse(report_path=f"[ERROR] Failed to clone repo: {e}")
    try:
        report_path = engine.run(repo_path)
    finally:
        if temp_dir and os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
    return RefactorResponse(report_path=report_path)
