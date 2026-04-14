from acoes import (
    abrir_navegador,
    abrir_apple_music,
    dizer_hora,
    dizer_data,
    verificar_internet,
    mostrar_bateria
)
from speaker import falar_erro, falar
from intents import detectar_intencao
from conversas import responder_conversa
from contexto import salvar_contexto


def executar_comando(comando):
    intencao = detectar_intencao(comando)

    if intencao == "hora":
        salvar_contexto(intencao, comando)
        dizer_hora()

    elif intencao == "data":
        salvar_contexto(intencao, comando)
        dizer_data()

    elif intencao == "internet":
        salvar_contexto(intencao, comando)
        verificar_internet()

    elif intencao == "bateria":
        salvar_contexto(intencao, comando)
        mostrar_bateria()

    elif intencao == "abrir_navegador":
        salvar_contexto(intencao, comando)
        abrir_navegador()

    elif intencao == "abrir_apple_music":
        salvar_contexto(intencao, comando)
        abrir_apple_music()

    else:
        resposta = responder_conversa(comando)

        if resposta:
            salvar_contexto("conversa", comando)
            falar(resposta)
        else:
            print(f"Alfred: comando não reconhecido -> {comando}")
            falar_erro()