def test_health():
    resposta = client.get("/health")

    assert resposta.status_code == 200

    assert resposta.json() == {
        "status": "ok"
    }


def test_api_analisar():
    resposta = client.post(
        "/analisar",
        json={
            "mensagem": "produto chegou quebrado"
        }

    )

    assert resposta.status_code == 200

    dados = resposta.json()

    assert dados["categoria"] == "troca"
    assert dados["prioridade"] == "alta"
    assert "confianca" in dados