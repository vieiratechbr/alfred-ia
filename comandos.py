from acoes import (
    abrir_navegador,
    abrir_apple_music,
    dizer_hora,
    dizer_data,
    verificar_internet,
    mostrar_bateria
)
from speaker import falar_erro
from intents import detectar_intencao
from conversas import responder_conversa


def executar_comando(comando):
    intencao = detectar_intencao(comando)

    if intencao == "hora":
        dizer_hora()

    elif intencao == "data":
        dizer_data()

    elif intencao == "internet":
        verificar_internet()

    elif intencao == "bateria":
        mostrar_bateria()

    elif intencao == "abrir_navegador":
        abrir_navegador()

    elif intencao == "abrir_apple_music":
        abrir_apple_music()

    else:
        resposta = responder_conversa(comando)

        if resposta:
            from speaker import falar
            falar(resposta)
        else:
            print(f"Alfred: comando não reconhecido -> {comando}")
            falar_erro()