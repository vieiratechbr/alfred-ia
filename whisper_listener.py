import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
from faster_whisper import WhisperModel

# carrega modelo (primeira vez demora)
model = WhisperModel("base", compute_type="int8")


def gravar_audio(duracao=4, fs=16000):
    print("Alfred: fale agora...")

    audio = sd.rec(int(duracao * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()

    write("audio.wav", fs, audio)
    return "audio.wav"


def ouvir_comando():
    arquivo = gravar_audio()

    segments, _ = model.transcribe(arquivo, language="pt")

    texto = ""
    for segment in segments:
        texto += segment.text

    texto = texto.strip().lower()

    print(f"Você disse: {texto}")
    return texto