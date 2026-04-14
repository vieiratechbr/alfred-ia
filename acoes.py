import os
import subprocess


def abrir_navegador():
    caminho_vivaldi = r"C:\Users\natha\AppData\Local\Vivaldi\Application\vivaldi.exe"

    if os.path.exists(caminho_vivaldi):
        subprocess.Popen([caminho_vivaldi])
        print("Alfred: abrindo o navegador.")
    else:
        print("Alfred: não encontrei o Vivaldi nesse caminho.")


def abrir_apple_music():
    try:
        os.startfile("shell:AppsFolder\\AppleInc.AppleMusicWin_nzyj5cx40ttqa!AppleMusic")
        print("Alfred: abrindo o Apple Music.")
    except Exception as erro:
        print(f"Alfred: não consegui abrir o Apple Music. Erro: {erro}")