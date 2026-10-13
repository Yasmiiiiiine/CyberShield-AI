import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

# Importation directe depuis le fichier analyzer.py
from analyzer import analyze_password, analyze_url, analyze_email_text

app = FastAPI(title="CyberShield AI API")

# Configuration CORS
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

# Route principale GET : Affiche directement l'interface front-end
@app.get("/", response_class=HTMLResponse)
index():
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    return "<h3>Bienvenue sur l'API CyberShield AI. Le fichier index.html est introuvable sur le serveur.</h3>"

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
