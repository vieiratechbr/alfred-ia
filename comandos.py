from acoes import abrir_navegador, abrir_apple_music


def executar_comando(comando):
    comando = comando.lower().strip()

    if comando == "abra o navegador":
        abrir_navegador()

    elif comando == "abra o apple music":
        abrir_apple_music()

    else:
        print("Alfred: comando não reconhecido.")