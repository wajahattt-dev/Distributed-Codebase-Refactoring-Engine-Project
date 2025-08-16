# Pydantic request/response DTOs
from pydantic import BaseModel

class RefactorRequest(BaseModel):
    repo_path: str

class RefactorResponse(BaseModel):
    report_path: str
