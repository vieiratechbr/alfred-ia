import random
from utils import normalizar_texto


def responder_conversa(texto):
    comando = normalizar_texto(texto)

    if any(p in comando for p in ["oi", "ola", "bom dia", "boa tarde", "boa noite"]):
        return random.choice([
            "Olá, senhor. Como posso ajudar?",
            "Saudações. Em que posso ser útil?",
            "Olá. Estou à disposição."
        ])

    if any(p in comando for p in ["tudo bem", "como voce esta", "como vai"]):
        return random.choice([
            "Tudo em ordem, senhor. E com você?",
            "Funcionando perfeitamente. Como posso ajudar?",
            "Tudo bem por aqui."
        ])

    if any(p in comando for p in ["obrigado", "valeu"]):
        return random.choice([
            "Sempre à disposição.",
            "Por nada, senhor.",
            "É um prazer ajudar."
        ])

    if any(p in comando for p in ["quem e voce", "o que voce faz"]):
        return random.choice([
            "Sou Alfred, seu assistente pessoal.",
            "Estou aqui para ajudar com suas tarefas.",
            "Sou seu assistente, pronto para ajudar no que precisar."
        ])

    return None