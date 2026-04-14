import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import json

q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(bytes(indata))


def ouvir_comando():
    modelo = Model("model")
    reconhecedor = KaldiRecognizer(modelo, 16000)

    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):

        print("Alfred: estou ouvindo...")

        while True:
            data = q.get()

            if reconhecedor.AcceptWaveform(data):
                resultado = json.loads(reconhecedor.Result())
                texto = resultado.get("text", "")
                
                if texto:
                    print(f"Você disse: {texto}")
                    return texto