import os
import subprocess
from speaker import falar_navegador, falar_music


def abrir_navegador():
    caminho_vivaldi = r"C:\Users\natha\AppData\Local\Vivaldi\Application\vivaldi.exe"

    if os.path.exists(caminho_vivaldi):
        subprocess.Popen([caminho_vivaldi])
        falar_navegador()
    else:
        print("Alfred: não encontrei o Vivaldi nesse caminho.")


def abrir_apple_music():
    try:
        os.startfile(r"shell:AppsFolder\AppleInc.AppleMusicWin_nzyj5cx40ttqa!App")
        falar_music()
    except Exception as erro:
        print("Alfred: não consegui abrir o Apple Music.")
        print(f"Erro técnico: {erro}")