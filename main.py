import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from analyzer import analyze_password, analyze_url, analyze_email_text

app = FastAPI(title="CyberShield AI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PasswordInput(BaseModel):
    password: str

class UrlInput(BaseModel):
    url: str

class EmailInput(BaseModel):
    email_content: str

@app.post("/analyze/password")
def api_analyze_password(data: PasswordInput):
    return analyze_password(data.password)

@app.post("/analyze/url")
def api_analyze_url(data: UrlInput):
    return analyze_url(data.url)

@app.post("/analyze/email")
def api_analyze_email(data: EmailInput):
    return analyze_email_text(data.email_content)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
