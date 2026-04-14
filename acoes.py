import os
import json
import socket
import subprocess
from pathlib import Path
from datetime import datetime
from urllib.parse import quote_plus

import psutil
import pyautogui

from speaker import (
    falar,
    falar_navegador,
    falar_music,
    falar_hora,
    falar_data,
    falar_internet_conectada,
    falar_internet_desconectada,
    falar_bateria,
    falar_bateria_indisponivel
)


CACHE_APPS = Path("apps_cache.json")

CAMINHOS_PADRAO = [
    r"C:\Program Files",
    r"C:\Program Files (x86)",
    os.path.expandvars(r"%LOCALAPPDATA%"),
    os.path.expandvars(r"%APPDATA%"),
]


def carregar_cache_apps():
    if CACHE_APPS.exists():
        with open(CACHE_APPS, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def salvar_cache_apps(cache):
    with open(CACHE_APPS, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)


def listar_apps_windows():
    try:
        comando = [
            "powershell",
            "-NoProfile",
            "-Command",
            "Get-StartApps | Select-Object Name, AppID | ConvertTo-Json -Depth 2"
        ]
        resultado = subprocess.run(
            comando,
            capture_output=True,
            text=True,
            encoding="utf-8"
        )

        if resultado.returncode != 0 or not resultado.stdout.strip():
            return []

        dados = json.loads(resultado.stdout)

        if isinstance(dados, dict):
            dados = [dados]

        return dados
    except Exception:
        return []


def encontrar_app_windows(nome_app):
    nome_app = nome_app.lower().strip()
    apps = listar_apps_windows()

    for app in apps:
        nome = app.get("Name", "").lower()
        app_id = app.get("AppID", "")

        if nome_app in nome:
            return {
                "tipo": "windows_app",
                "nome": app.get("Name", nome_app),
                "app_id": app_id
            }

    return None


def encontrar_executavel(nome_app):
    nome_app = nome_app.lower().strip()

    for pasta in CAMINHOS_PADRAO:
        if not os.path.exists(pasta):
            continue

        for root, dirs, files in os.walk(pasta):
            for file in files:
                nome_arquivo = file.lower()
                if nome_arquivo.endswith(".exe") and nome_app in nome_arquivo:
                    return {
                        "tipo": "exe",
                        "nome": file,
                        "caminho": os.path.join(root, file)
                    }

    return None


def encontrar_aplicativo(nome_app):
    cache = carregar_cache_apps()
    chave = nome_app.lower().strip()

    if chave in cache:
        return cache[chave]

    resultado = encontrar_app_windows(nome_app)

    if not resultado:
        resultado = encontrar_executavel(nome_app)

    if resultado:
        cache[chave] = resultado
        salvar_cache_apps(cache)

    return resultado


def abrir_aplicativo(nome_app):
    resultado = encontrar_aplicativo(nome_app)

    if not resultado:
        falar(f"Não encontrei o aplicativo {nome_app} no sistema.")
        return

    try:
        if resultado["tipo"] == "windows_app":
            falar(f"Claro, senhor. Abrindo {resultado['nome']}.")
            os.startfile(f"shell:AppsFolder\\{resultado['app_id']}")
            return

        if resultado["tipo"] == "exe":
            falar(f"Claro, senhor. Abrindo {nome_app}.")
            subprocess.Popen([resultado["caminho"]])
            return

        falar(f"Não consegui abrir o aplicativo {nome_app}.")
    except Exception:
        falar(f"Não consegui abrir o aplicativo {nome_app}.")


def abrir_navegador():
    caminho_vivaldi = r"C:\Users\natha\AppData\Local\Vivaldi\Application\vivaldi.exe"

    if os.path.exists(caminho_vivaldi):
        falar_navegador()
        subprocess.Popen([caminho_vivaldi])
    else:
        falar("Não encontrei o navegador configurado.")


def abrir_site_no_navegador(url, nome_site):
    caminho_vivaldi = r"C:\Users\natha\AppData\Local\Vivaldi\Application\vivaldi.exe"

    if os.path.exists(caminho_vivaldi):
        falar(f"Claro, senhor. Abrindo {nome_site}.")
        subprocess.Popen([caminho_vivaldi, url])
    else:
        falar("Não encontrei o navegador configurado.")


def abrir_youtube():
    abrir_site_no_navegador("https://www.youtube.com", "o YouTube")


def abrir_google():
    abrir_site_no_navegador("https://www.google.com", "o Google")


def pesquisar_no_google(termo):
    caminho_vivaldi = r"C:\Users\natha\AppData\Local\Vivaldi\Application\vivaldi.exe"
    url = f"https://www.google.com/search?q={quote_plus(termo)}"

    if os.path.exists(caminho_vivaldi):
        falar(f"Claro, senhor. Pesquisando por {termo} no Google.")
        subprocess.Popen([caminho_vivaldi, url])
    else:
        falar("Não encontrei o navegador configurado.")


def pesquisar_no_youtube(termo):
    caminho_vivaldi = r"C:\Users\natha\AppData\Local\Vivaldi\Application\vivaldi.exe"
    url = f"https://www.youtube.com/results?search_query={quote_plus(termo)}"

    if os.path.exists(caminho_vivaldi):
        falar(f"Como desejar. Pesquisando por {termo} no YouTube.")
        subprocess.Popen([caminho_vivaldi, url])
    else:
        falar("Não encontrei o navegador configurado.")


def abrir_apple_music():
    try:
        falar_music()
        os.startfile(r"shell:AppsFolder\AppleInc.AppleMusicWin_nzyj5cx40ttqa!App")
    except Exception:
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
    except OSError:
        falar_internet_desconectada()


def mostrar_bateria():
    bateria = psutil.sensors_battery()

    if bateria is None:
        falar_bateria_indisponivel()
        return

    porcentagem = int(bateria.percent)
    carregando = bateria.power_plugged
    falar_bateria(porcentagem, carregando)


def aumentar_volume(passos=5):
    for _ in range(passos):
        pyautogui.press("volumeup")
    falar("Aumentando o volume.")


def diminuir_volume(passos=5):
    for _ in range(passos):
        pyautogui.press("volumedown")
    falar("Diminuindo o volume.")


def mutar_volume():
    pyautogui.press("volumemute")
    falar("Alternando o modo mudo.")


def alternar_play_pause():
    pyautogui.press("playpause")
    falar("Alternando a reprodução de mídia.")


def proxima_musica():
    pyautogui.press("nexttrack")
    falar("Pulando para a próxima faixa.")


def musica_anterior():
    pyautogui.press("prevtrack")
    falar("Voltando para a faixa anterior.")