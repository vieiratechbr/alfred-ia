import subprocess
import tempfile
import random
import winsound
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PIPER_DIR = BASE_DIR / "piper"
PIPER_EXE = PIPER_DIR / "piper.exe"
PIPER_MODEL = PIPER_DIR / "pt_BR-faber-medium.onnx"


def falar(texto):
    print(f"Alfred: {texto}")

    wav_path = None

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
            cwd=str(PIPER_DIR)
        )

        _, stderr = processo.communicate(input=texto)

        if processo.returncode != 0:
            print("Erro no Piper:")
            print(stderr)
            return

        # Toca o áudio diretamente, sem abrir player externo
        winsound.PlaySound(wav_path, winsound.SND_FILENAME)

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