import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel
import time

modelo = None


def carregar_modelo():
    global modelo

    if modelo is None:
        print("Alfred: carregando modelo de voz...")
        modelo = WhisperModel("small", compute_type="int8")

    return modelo


def ouvir_comando():
    modelo = carregar_modelo()

    fs = 16000
    duracao = 4

    print("Alfred: prepare-se para falar...")
    time.sleep(0.5)

    print("Alfred: fale agora...")
    audio = sd.rec(int(duracao * fs), samplerate=fs, channels=1, dtype="float32")
    sd.wait()

    audio = np.squeeze(audio)

    segmentos, _ = modelo.transcribe(audio, language="pt")

    texto = ""

    for segmento in segmentos:
        texto += segmento.text

    texto = texto.strip().lower()

    print(f"Você disse: {texto}")

    return texto