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
        r"\bAlfred\b": "Álfred",
        r"\bVivaldi\b": "Vivaldi",
        r"\bApple Music\b": "Épol Miuzic",
        r"\bApple\b": "Épol",
        r"\bMusic\b": "Miuzic",
        r"\bWindows\b": "Uíndous",
        r"\bChrome\b": "Crome",
        r"\bYouTube\b": "Iútchubi",
        r"\bGoogle\b": "Gugou",
        r"\bSpotify\b": "Spotifai",
        r"\bDiscord\b": "Discor",
        r"\bPython\b": "Paiton",
        r"\bJavaScript\b": "Javascipt",
        r"\bNode\b": "Nôde",
        r"\bVS Code\b": "V S Code",
    }

    texto_ajustado = texto

    for padrao, substituto in substituicoes.items():
        texto_ajustado = re.sub(
            padrao,
            substituto,
            texto_ajustado,
            flags=re.IGNORECASE
        )

    return texto_ajustado


def falar(texto: str):
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


def obter_saudacao_por_horario() -> str:
    hora_atual = datetime.now().hour

    if hora_atual < 12:
        return "Bom dia"
    elif hora_atual < 18:
        return "Boa tarde"
    else:
        return "Boa noite"


def falar_saudacao_inicial():
    saudacao = obter_saudacao_por_horario()

    frases = [
        f"{saudacao}. Alfred online e à sua disposição.",
        f"{saudacao}. Estou pronto para ajudar.",
        f"{saudacao}. Sistemas ativos. Como posso ajudar?",
    ]

    falar(random.choice(frases))


def falar_navegador():
    respostas = [
        "Claro, senhor. Abrindo o navegador.",
        "Como desejar. Já estou abrindo o navegador.",
        "Imediatamente. O navegador será iniciado.",
        "Perfeitamente. Abrindo o Vivaldi agora."
    ]
    falar(random.choice(respostas))


def falar_music():
    respostas = [
        "Com prazer. Abrindo o reprodutor de música.",
        "Já estou iniciando sua música, senhor.",
        "Perfeitamente. Preparando o Apple Music.",
        "Como desejar. Música iniciando agora."
    ]
    falar(random.choice(respostas))


def falar_erro():
    respostas = [
        "Peço desculpas, senhor. Não compreendi o comando.",
        "Receio não ter entendido. Poderia repetir?",
        "Desculpe, não consegui interpretar o pedido.",
        "Não reconheci o comando. Pode tentar novamente?"
    ]
    falar(random.choice(respostas))