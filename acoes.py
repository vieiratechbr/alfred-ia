import os
import subprocess
import socket
import psutil
import pyautogui
from datetime import datetime
from urllib.parse import quote_plus

from speaker import (
    falar_navegador,
    falar_music,
    falar_hora,
    falar_data,
    falar_internet_conectada,
    falar_internet_desconectada,
    falar_bateria,
    falar_bateria_indisponivel,
    falar
)


CAMINHOS_PADRAO = [
    r"C:\Program Files",
    r"C:\Program Files (x86)",
    os.path.expandvars(r"%LOCALAPPDATA%"),
    os.path.expandvars(r"%APPDATA%"),
]


def encontrar_executavel(nome_app):
    nome_app = nome_app.lower()

    for pasta in CAMINHOS_PADRAO:
        for root, dirs, files in os.walk(pasta):
            for file in files:
                if file.lower().endswith(".exe") and nome_app in file.lower():
                    return os.path.join(root, file)
    return None


def abrir_aplicativo(nome_app):
    caminho = encontrar_executavel(nome_app)

    if caminho:
        falar(f"Claro, senhor. Abrindo {nome_app}.")
        subprocess.Popen([caminho])
    else:
        falar(f"Não encontrei o aplicativo {nome_app} no sistema.")


def abrir_navegador():
    caminho_vivaldi = r"C:\Users\natha\AppData\Local\Vivaldi\Application\vivaldi.exe"

    if os.path.exists(caminho_vivaldi):
        falar_navegador()
        subprocess.Popen([caminho_vivaldi])


def abrir_site_no_navegador(url, nome_site):
    caminho_vivaldi = r"C:\Users\natha\AppData\Local\Vivaldi\Application\vivaldi.exe"

    if os.path.exists(caminho_vivaldi):
        falar(f"Claro, senhor. Abrindo {nome_site}.")
        subprocess.Popen([caminho_vivaldi, url])


def abrir_youtube():
    abrir_site_no_navegador("https://www.youtube.com", "o YouTube")


def abrir_google():
    abrir_site_no_navegador("https://www.google.com", "o Google")


def pesquisar_no_google(termo):
    caminho_vivaldi = r"C:\Users\natha\AppData\Local\Vivaldi\Application\vivaldi.exe"
    url = f"https://www.google.com/search?q={quote_plus(termo)}"

    if os.path.exists(caminho_vivaldi):
        falar(f"Pesquisando por {termo}.")
        subprocess.Popen([caminho_vivaldi, url])


def pesquisar_no_youtube(termo):
    caminho_vivaldi = r"C:\Users\natha\AppData\Local\Vivaldi\Application\vivaldi.exe"
    url = f"https://www.youtube.com/results?search_query={quote_plus(termo)}"

    if os.path.exists(caminho_vivaldi):
        falar(f"Buscando {termo} no YouTube.")
        subprocess.Popen([caminho_vivaldi, url])


def abrir_apple_music():
    try:
        falar_music()
        os.startfile(r"shell:AppsFolder\AppleInc.AppleMusicWin_nzyj5cx40ttqa!App")
    except:
        falar("Não consegui abrir o Apple Music.")


def dizer_hora():
    agora = datetime.now()
    hora = agora.strftime("%H:%M")
    falar_hora(hora)


def dizer_data():
    agora = datetime.now()

    dias_semana = [
        "segunda-feira", "terça-feira", "quarta-feira",
        "quinta-feira", "sexta-feira", "sábado", "domingo"
    ]

    meses = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]

    dia_semana = dias_semana[agora.weekday()]
    dia = agora.day
    mes = meses[agora.month - 1]

    data_texto = f"{dia_semana}, dia {dia} de {mes}"
    falar_data(data_texto)


def verificar_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        falar_internet_conectada()
    except:
        falar_internet_desconectada()


def mostrar_bateria():
    bateria = psutil.sensors_battery()

    if bateria is None:
        falar_bateria_indisponivel()
        return

    porcentagem = int(bateria.percent)
    carregando = bateria.power_plugged
    falar_bateria(porcentagem, carregando)


def aumentar_volume():
    for _ in range(5):
        pyautogui.press("volumeup")
    falar("Aumentando o volume.")


def diminuir_volume():
    for _ in range(5):
        pyautogui.press("volumedown")
    falar("Diminuindo o volume.")


def mutar_volume():
    pyautogui.press("volumemute")
    falar("Modo mudo ativado.")


def alternar_play_pause():
    pyautogui.press("playpause")
    falar("Controle de mídia alternado.")


def proxima_musica():
    pyautogui.press("nexttrack")
    falar("Próxima música.")


def musica_anterior():
    pyautogui.press("prevtrack")
    falar("Música anterior.")