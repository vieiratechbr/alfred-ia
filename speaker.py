import pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate", 180)   # velocidade da fala
engine.setProperty("volume", 1.0) # volume de 0.0 a 1.0


def falar(texto):
    print(f"Alfred: {texto}")
    engine.say(texto)
    engine.runAndWait()