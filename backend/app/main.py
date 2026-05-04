from fastapi import FastAPI
from app.models import EmailRequest, AnalysisResponse
from app.scorer import analyze

app = FastAPI(title="Malicious Email Scorer")

@app.get("/")
def root():
    return {"message": "API is running"}

@app.post("/analyze", response_model=AnalysisResponse)
def analyze_email(email: EmailRequest):
    return analyze(email)