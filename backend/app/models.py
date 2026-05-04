from pydantic import BaseModel
from typing import List


class EmailRequest(BaseModel):
    subject: str
    sender: str
    body: str


class AnalysisResponse(BaseModel):
    score: int
    verdict: str
    recommendation: str
    reasons: List[str]