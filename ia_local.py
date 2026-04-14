from ollama import chat


def perguntar_ia_local(texto):
    try:
        resposta = chat(
            model="qwen2.5:3b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Você é Alfred, um assistente pessoal elegante, educado e natural. "
                        "Responda sempre em português do Brasil. "
                        "Seja claro, humano e objetivo. "
                        "Evite respostas longas demais. "
                        "Quando não souber algo com segurança, diga isso com honestidade."
                    ),
                },
                {
                    "role": "user",
                    "content": texto,
                },
            ],
        )

        return resposta["message"]["content"].strip()

    except Exception as erro:
        print(f"Erro IA local: {erro}")
        return None