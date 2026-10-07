# SmartSupport AI

MVP para demonstrar IA, Engenharia de Software, Qualidade de Software,
gestão de projeto e transformação digital em uma única prática.

## O produto

O usuário digita uma mensagem de atendimento. A aplicação:
1. representa o texto com TF-IDF;
2. usa aprendizado supervisionado para classificar em `entrega`, `pagamento` ou `troca`;
3. usa uma regra heurística simples para prioridade;
4. devolve categoria, prioridade e confiança por uma API REST;
5. exibe o resultado no navegador;
6. possui testes automatizados com Pytest.

> O dataset é propositalmente pequeno e didático. O modelo não deve ser tratado
> como sistema de produção nem como classificador de alta precisão.

## Requisitos

- Python 3.10+
- navegador
- terminal

## Instalação

```bash
python -m venv .venv
source .venv/bin/activate
```

No Windows:

```bash
.venv\Scripts\activate
```

Instale:

```bash
pip install -r requirements.txt
```

## Executar

```bash
uvicorn main:app --reload
```

Abra `http://127.0.0.1:8000`.

Documentação automática da API:
`http://127.0.0.1:8000/docs`

## Executar testes

```bash
pytest -v
```

## Arquitetura

```text
Usuário
  |
  v
HTML/CSS/JavaScript
  |
  | HTTP/JSON
  v
FastAPI
  |
  v
analisar_mensagem()
  |
  +--> TF-IDF + Logistic Regression
  |
  +--> Regra heurística de prioridade
  |
  v
JSON de resposta
```

## Requisitos

RF01 — receber uma mensagem do cliente.  
RF02 — classificar a mensagem.  
RF03 — retornar categoria.  
RF04 — indicar prioridade.  
RF05 — apresentar uma medida de confiança.

RNF01 — possuir interface web simples.  
RNF02 — comunicação cliente-servidor em HTTP/JSON.  
RNF03 — possuir testes automatizados.
