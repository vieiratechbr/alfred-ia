from comandos import executar_comando
from whisper_listener import ouvir_comando


def main():
    print("=== Alfred V1 (voz) ===")

    while True:
        comando = ouvir_comando()
        executar_comando(comando)


if __name__ == "__main__":
    main()