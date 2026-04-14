import subprocess
import tempfile
import random
import winsound
import re
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent
PIPER_DIR = BASE_DIR / "piper"
PIPER_EXE = PIPER_DIR / "piper.exe"
PIPER_MODEL = PIPER_DIR / "pt_BR-faber-medium.onnx"


def ajustar_pronuncia(texto: str) -> str:
    substituicoes = {
        r"\bAlfred\b": "Alfredi",
        r"\bVivaldi\b": "Vivaldi",
        r"\bApple Music\b": "Épol Miuzic",
        r"\bMusic\b": "Miuzic",
        r"\bWindows\b": "Uíndous",
    }

    texto_ajustado = texto
    for padrao, substituto in substituicoes.items():
        texto_ajustado = re.sub(padrao, substituto, texto_ajustado, flags=re.IGNORECASE)

    return texto_ajustado


def falar(texto):
    print(f"Alfred: {texto}")

    wav_path = None

    try:
        texto_para_fala = ajustar_pronuncia(texto)

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

        _, stderr = processo.communicate(input=texto_para_fala)

        if processo.returncode != 0:
            print("Erro no Piper:")
            print(stderr)
            return

        winsound.PlaySound(wav_path, winsound.SND_FILENAME)

    except Exception as erro:
        print(f"Erro no Piper: {erro}")


def obter_saudacao_por_horario():
    hora_atual = datetime.now().hour

    if hora_atual < 12:
        return "Bom dia"
    elif hora_atual < 18:
        return "Boa tarde"
    else:
        return "Boa noite"


def falar_saudacao_inicial():
    saudacao = obter_saudacao_por_horario()
    falar(f"{saudacao}. Tudo bem? Alfred iniciado e pronto para ajudar.")


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