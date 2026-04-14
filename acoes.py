import os
import subprocess
from speaker import falar


def abrir_navegador():
    caminho_vivaldi = r"C:\Users\natha\AppData\Local\Vivaldi\Application\vivaldi.exe"

    if os.path.exists(caminho_vivaldi):
        subprocess.Popen([caminho_vivaldi])
        falar("Abrindo o navegador.")
    else:
        falar("Não encontrei o Vivaldi nesse caminho.")


def abrir_apple_music():
    try:
        os.startfile(r"shell:AppsFolder\AppleInc.AppleMusicWin_nzyj5cx40ttqa!App")
        falar("Abrindo o Apple Music.")
    except Exception as erro:
        falar("Não consegui abrir o Apple Music.")
        print(f"Erro técnico: {erro}")  