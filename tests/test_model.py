import pytest
from model import analisar_mensagem

def test_mensagem_vazia():
    with pytest.raises(ValueError):
        analisar_mensagem("")

def test_retorna_campos_esperados():
    resultado = analisar_mensagem("meu pedido não chegou")
    assert "categoria" in resultado
    assert "prioridade" in resultado
    assert "confianca" in resultado

def test_prioridade_alta_para_cobranca_duplicada():
    resultado = analisar_mensagem("fui cobrado duas vezes")
    assert resultado["prioridade"] == "alta"

def test_classifica_exemplo_de_troca():
    resultado = analisar_mensagem("produto chegou quebrado")
    assert resultado["categoria"] == "troca"
