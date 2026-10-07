import pytest
from model import analisar_mensagem

def test_mensagem_vazia():
    with pytest.raises(ValueError):
        analisar_mensagem("")

def test_mensagem_com_espacos_deve_gerar_erro():
    with pytest.raises(ValueError):
        analisar_mensagem("        ")

def test_resultado_deve_ser_dicionario():
    resultado = analisar_mensagem(
        "meu pedido não chegou"
    )
    assert isinstance(resultado, dict)

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

def test_classificacao_pagamento():
    resultado = analisar_mensagem(
        "meu cartão foi recusado"
    )

    assert resultado["categoria"] == "pagamento"

def test_confianca_deve_estar_entre_zero_e_um():
    resultado = analisar_mensagem(
        "meu cartão foi recusado"
    )

    assert 0 <= resultado["confianca"] <= 1

def test_confianca_deve_ser_numero():
    resultado = analisar_mensagem(
        "meu cartao foi recusado"
    )

    assert isinstance(
        resultado["confianca"],
        float
    )

def test_mensagem_com_espacos_extras():
    resultado = analisar_mensagem(
        "   meu pedido não chegou   "
    )

    assert resultado["categoria"] == "entrega"

