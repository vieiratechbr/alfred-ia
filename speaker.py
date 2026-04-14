import pyttsx3


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