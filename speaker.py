import subprocess
import tempfile
import os
import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PIPER_EXE = BASE_DIR / "piper" / "piper.exe"
PIPER_MODEL = BASE_DIR / "piper" / "pt_BR-faber-medium.onnx"


def falar(texto):
    print(f"Alfred: {texto}")

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
            wav_path = f.name

        comando = [
            str(PIPER_EXE),
            "-m", str(PIPER_MODEL),
            "-f", wav_path
        ]

        processo = subprocess.Popen(
            comando,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=str(BASE_DIR / "piper")
        )

        stdout, stderr = processo.communicate(input=texto)

        if processo.returncode != 0:
            print("Erro no Piper:")
            print(stderr)
            return

        os.startfile(wav_path)

    except Exception as erro:
        print(f"Erro no Piper: {erro}")


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