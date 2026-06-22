from fastapi import FastAPI, UploadFile, Form
from pydantic import BaseModel

app = FastAPI(title="Profile Analyzer")

class Analysis(BaseModel):
    skills: list[str]
    experience: list[dict]

@app.post("/analyze")
async def analyze(resume: UploadFile = None, linkedin_url: str = Form(None)):
    # TODO: Implement parsing
    return {"status": "success", "data": {"skills": ["Python", "FastAPI"], "experience": []}}
