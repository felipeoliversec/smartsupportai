from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from model import analisar_mensagem



app = FastAPI(title="SmartSupport AI", version="1.0.0")

class MensagemEntrada(BaseModel):
    mensagem: str = Field(min_length=1, max_length=500)

@app.get("/")
def pagina():
    return FileResponse("static/index.html")

@app.post("/analisar")
def analisar(dados: MensagemEntrada):
    try:
        return analisar_mensagem(dados.mensagem)
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))

@app.get("/health")
def health():
    return {"status": "ok"}
