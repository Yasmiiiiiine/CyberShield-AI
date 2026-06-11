from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse
from pydantic import BaseModel
from analyzer import analyze_password, analyze_url, analyze_email_text

# Initialisation de l'API FastAPI
app = FastAPI(title="CyberShield AI API")

# Configuration CORS pour autoriser les requêtes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modèles de données Pydantic pour valider les entrées
class PasswordInput(BaseModel):
    password: str

class UrlInput(BaseModel):
    url: str

class EmailInput(BaseModel):
    email_content: str

# Route principale : Sert l'interface graphique (Front-end)
@app.get("/", response_class=HTMLResponse)
def serve_frontend():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

# Route API : Analyse de mot de passe
@app.post("/analyze/password")
def api_analyze_password(data: PasswordInput):
    return analyze_password(data.password)

# Route API : Analyse d'URL
@app.post("/analyze/url")
def api_analyze_url(data: UrlInput):
    return analyze_url(data.url)

# Route API : Analyse de contenu d'e-mail suspect
@app.post("/analyze/email")
def api_analyze_email(data: EmailInput):
    return analyze_email_text(data.email_content)

# Bloc de lancement du serveur (toujours à la toute fin du fichier)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)