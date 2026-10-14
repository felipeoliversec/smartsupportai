from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    resposta = client.get("/health")

    assert resposta.status_code == 200
    assert resposta.json() == {"status": "ok"}

def test_api_sem_mensagem():
    resposta = client.post("/analisar", json={})

    assert resposta.status_code == 422

def test_api_mensagem_vazia():
    resposta = client.post(
        "/analisar",
        json={"mensagem": ""}
    )

    assert resposta.status_code == 422