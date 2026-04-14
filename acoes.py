import os
import subprocess
from datetime import datetime
from speaker import falar
from speaker import falar_navegador, falar_music


def abrir_navegador():
    caminho_vivaldi = r"C:\Users\natha\AppData\Local\Vivaldi\Application\vivaldi.exe"

    if os.path.exists(caminho_vivaldi):
        falar_navegador()
        subprocess.Popen([caminho_vivaldi])
    else:
        print("Alfred: não encontrei o Vivaldi nesse caminho.")


def abrir_apple_music():
    try:
        falar_music()
        os.startfile(r"shell:AppsFolder\AppleInc.AppleMusicWin_nzyj5cx40ttqa!App")
    except Exception as erro:
        print("Alfred: não consegui abrir o Apple Music.")
        print(f"Erro técnico: {erro}")

def dizer_hora():
    agora = datetime.now()
    hora = agora.strftime("%H:%M")

    falar(f"Agora são {hora}.")


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

    falar(f"Hoje é {dia_semana}, dia {dia} de {mes}.")