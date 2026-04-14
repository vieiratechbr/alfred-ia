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

    frases = [
        f"{saudacao}. Alfred online e à sua disposição.",
        f"{saudacao}. Estou pronto para ajudar.",
        f"{saudacao}. Sistemas ativos. Como posso ajudar?"
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


def falar_hora(hora):
    respostas = [
        f"Claro, senhor. Agora são {hora}.",
        f"Neste momento, são {hora}.",
        f"Acabei de verificar. Agora são {hora}.",
        f"Agora são exatamente {hora}."
    ]
    falar(random.choice(respostas))


def falar_data(data_texto):
    respostas = [
        f"Hoje é {data_texto}.",
        f"Claro. Hoje é {data_texto}.",
        f"Acabei de verificar. Hoje é {data_texto}.",
        f"A data de hoje é {data_texto}."
    ]
    falar(random.choice(respostas))


def falar_internet_conectada():
    respostas = [
        "Sim, senhor. A conexão com a internet está ativa.",
        "Tudo certo. A internet está funcionando normalmente.",
        "Acabei de verificar. A conexão está ativa.",
        "Sim. Há acesso à internet neste momento."
    ]
    falar(random.choice(respostas))


def falar_internet_desconectada():
    respostas = [
        "No momento, não detectei conexão com a internet.",
        "Receio que a conexão com a internet esteja indisponível.",
        "Acabei de verificar e não há acesso à internet.",
        "Não detectei internet ativa neste momento."
    ]
    falar(random.choice(respostas))


def falar_bateria(porcentagem, carregando):
    if carregando:
        respostas = [
            f"A bateria está em {porcentagem} por cento e o equipamento está carregando.",
            f"No momento, a bateria está em {porcentagem} por cento e conectada à energia.",
            f"A carga atual é de {porcentagem} por cento, e a bateria está carregando."
        ]
    else:
        respostas = [
            f"A bateria está em {porcentagem} por cento.",
            f"No momento, restam {porcentagem} por cento de bateria.",
            f"A carga atual da bateria é de {porcentagem} por cento."
        ]

    falar(random.choice(respostas))


def falar_bateria_indisponivel():
    respostas = [
        "Não consegui acessar as informações da bateria.",
        "Receio que eu não consiga verificar a bateria neste momento.",
        "Não foi possível obter os dados da bateria agora."
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