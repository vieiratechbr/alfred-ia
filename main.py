from comandos import executar_comando


def main():
    print("=== Alfred V1 ===")
    print("Digite um comando para testar.")
    print("Exemplos:")
    print("- abra o navegador")
    print("- abra o Apple Music")
    print()

    comando = input("Você: ")
    executar_comando(comando)


if __name__ == "__main__":
    main()