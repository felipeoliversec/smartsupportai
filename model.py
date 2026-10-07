from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

DADOS = [
    ("meu pedido não chegou", "entrega"),
    ("onde está minha encomenda", "entrega"),
    ("a entrega está atrasada", "entrega"),
    ("não recebi meu produto", "entrega"),
    ("meu pacote ainda não chegou", "entrega"),
    ("quero rastrear meu pedido", "entrega"),

    ("meu cartão foi recusado", "pagamento"),
    ("não consigo fazer o pagamento", "pagamento"),
    ("fui cobrado duas vezes", "pagamento"),
    ("pagamento não foi aprovado", "pagamento"),
    ("problema para pagar", "pagamento"),
    ("pix não foi confirmado", "pagamento"),

    ("produto chegou quebrado", "troca"),
    ("quero trocar meu produto", "troca"),
    ("produto veio com defeito", "troca"),
    ("recebi o tamanho errado", "troca"),
    ("quero devolver o produto", "troca"),
    ("produto diferente do comprado", "troca"),
]

textos = [texto for texto, _ in DADOS]
categorias = [categoria for _, categoria in DADOS]

modelo = Pipeline([
    ("tfidf", TfidfVectorizer(lowercase=True, ngram_range=(1, 2))),
    ("classificador", LogisticRegression(max_iter=1000, random_state=42))
])

modelo.fit(textos, categorias)

def analisar_mensagem(mensagem: str) -> dict:
    mensagem = mensagem.strip()
    if not mensagem:
        raise ValueError("Mensagem obrigatória")

    categoria = modelo.predict([mensagem])[0]
    probabilidades = modelo.predict_proba([mensagem])[0]
    confianca = float(max(probabilidades))

    termos_urgentes = [
        "urgente", "cobrado duas vezes", "fraude",
        "não recebi", "nao recebi", "quebrado"
    ]
    prioridade = "alta" if any(t in mensagem.lower() for t in termos_urgentes) else "normal"

    return {
        "categoria": categoria,
        "prioridade": prioridade,
        "confianca": round(confianca, 2)
    }
