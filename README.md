# SmartSupport AI — laboratório interdisciplinar de 2 horas

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

## Requisitos didáticos

RF01 — receber uma mensagem do cliente.  
RF02 — classificar a mensagem.  
RF03 — retornar categoria.  
RF04 — indicar prioridade.  
RF05 — apresentar uma medida de confiança.

RNF01 — possuir interface web simples.  
RNF02 — comunicação cliente-servidor em HTTP/JSON.  
RNF03 — possuir testes automatizados.

## Roteiro da live — 120 minutos

### 0–10 min — Problema e transformação digital
Apresente uma loja que recebe muitas mensagens e precisa encaminhá-las.
Conecte com CRM, e-commerce, automação e transformação digital.

### 10–20 min — Requisitos e processo
Apresente RF01–RF05 e a user story:
“Como atendente, quero classificar mensagens automaticamente para encaminhar
cada solicitação ao setor adequado.”

Mini-backlog: modelo -> API -> interface -> testes.

### 20–30 min — Arquitetura
Desenhe: Navegador -> API -> Serviço de IA -> resultado.
Explique separação de responsabilidades e modularidade.

### 30–50 min — IA
Abra `model.py`.
Explique dataset rotulado = aprendizado supervisionado.
Mostre texto -> TF-IDF -> vetor -> classificador -> categoria.
Execute algumas chamadas no terminal/Python.

Conexões conceituais rápidas:
- K-Means: alternativa não supervisionada para encontrar grupos.
- árvore/rede neural: outros modelos possíveis.
- derivadas: redes neurais ajustam parâmetros minimizando uma função de erro.
- fuzzy: níveis de confiança podem ser pensados além de verdadeiro/falso.
- ética: dataset pequeno pode gerar erros e vieses; baixa confiança deve permitir revisão humana.

### 50–70 min — API REST
Abra `main.py`.
Explique GET, POST, JSON, validação e endpoint `/analisar`.
Inicie com `uvicorn main:app --reload`.
Teste também em `/docs`.

### 70–85 min — Front-end
Abra `static/index.html`.
Mostre HTML, CSS, JavaScript e `fetch`.
Envie mensagens pelo navegador.

### 85–105 min — Qualidade
Abra `tests/test_model.py`.
Explique caixa preta e teste unitário.
Execute `pytest -v`.
Mostre RED -> GREEN alterando temporariamente uma expectativa e corrigindo-a.
Explique regressão: testes existentes detectam quebra após mudanças.

### 105–115 min — Git/DevOps
Demonstre:
`git init`
`git add .`
`git commit -m "feat: cria SmartSupport AI"`
Explique que CI pode executar `pytest` automaticamente a cada push.

### 115–120 min — Fechamento
Peça mensagens ao público e teste ao vivo.
Discuta onde o produto poderia integrar WhatsApp, CRM, ERP, nuvem e no-code.

## Perguntas para envolver o público

- “Isso é aprendizado supervisionado ou não supervisionado?”
- “O que deveria acontecer se a confiança fosse muito baixa?”
- “Qual teste vocês criariam agora?”
- “Que requisito de segurança está faltando?”
- “Como integraríamos isso a um CRM?”
- “Onde entraria uma IA generativa?”

## Desafio final

Adicione uma quarta categoria chamada `cancelamento`, inclua pelo menos quatro
exemplos no dataset e crie um teste automatizado para ela.
