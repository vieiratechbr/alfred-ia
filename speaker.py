import pyttsx3
import random


def falar(texto):
    print(f"Alfred: {texto}")

    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 180)
        engine.setProperty("volume", 1.0)

        engine.say(texto)
        engine.runAndWait()
        engine.stop()

    except Exception as erro:
        print(f"Erro na fala do Alfred: {erro}")


def falar_navegador():
    respostas = [
        "Abrindo o navegador.",
        "Já estou abrindo o Vivaldi.",
        "Navegador sendo iniciado.",
        "Claro, abrindo o navegador agora."
    ]
    falar(random.choice(respostas))


def falar_music():
    respostas = [
        "Abrindo o Apple Music.",
        "Iniciando sua música.",
        "Apple Music pronto para uso.",
        "Já estou abrindo o Apple Music."
    ]
    falar(random.choice(respostas))


def falar_erro():
    respostas = [
        "Desculpe, não entendi o comando.",
        "Pode repetir, por favor?",
        "Não reconheci o que você disse.",
        "Não consegui entender esse comando."
    ]
    falar(random.choice(respostas))