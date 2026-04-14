import os
import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel

model = None


def carregar_modelo():
    global model

    if model is None:
        caminho_modelo = os.path.join("models", "faster-whisper-tiny")
        print("Alfred: carregando modelo local de voz...")
        model = WhisperModel(caminho_modelo, compute_type="int8")

    return model


def gravar_audio(duracao=4, fs=16000):
    print("Alfred: fale agora...")

    audio = sd.rec(int(duracao * fs), samplerate=fs, channels=1, dtype="int16")
    sd.wait()

    write("audio.wav", fs, audio)
    return "audio.wav"


def ouvir_comando():
    modelo = carregar_modelo()
    arquivo = gravar_audio()

    segments, _ = modelo.transcribe(arquivo, language="pt")

    texto = ""
    for segment in segments:
        texto += segment.text

    texto = texto.strip().lower()
    print(f"Você disse: {texto}")

    return texto