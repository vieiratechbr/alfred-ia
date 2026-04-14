import keyboard
from comandos import executar_comando
from whisper_listener import ouvir_comando
from speaker import falar_saudacao_inicial


def main():
    print("=== Alfred V1 (push-to-talk) ===")
    print("Pressione F8 para falar com o Alfred...")

    falar_saudacao_inicial()

    while True:
        keyboard.wait("F8")

        print("\nAlfred ativado...")
        comando = ouvir_comando()
        executar_comando(comando)

        print("\nPressione F8 novamente...")


if __name__ == "__main__":
    main()