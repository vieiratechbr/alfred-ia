from acoes import (
    abrir_aplicativo,
    abrir_navegador,
    abrir_youtube,
    abrir_google,
    pesquisar_no_google,
    pesquisar_no_youtube,
    abrir_apple_music,
    dizer_hora,
    dizer_data,
    verificar_internet,
    mostrar_bateria,
    aumentar_volume,
    diminuir_volume,
    mutar_volume,
    alternar_play_pause,
    proxima_musica,
    musica_anterior
)
from speaker import falar_erro, falar
from intents import detectar_intencao
from conversas import responder_conversa
from contexto import salvar_contexto
from ia_local import perguntar_ia_local


def executar_comando(comando):
    resultado = detectar_intencao(comando)

    if resultado:
        intencao = resultado["intent"]
        params = resultado.get("params", {})
    else:
        intencao = None
        params = {}

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

    elif intencao == "abrir_youtube":
        salvar_contexto(intencao, comando)
        abrir_youtube()

    elif intencao == "abrir_google":
        salvar_contexto(intencao, comando)
        abrir_google()

    elif intencao == "pesquisar_google":
        salvar_contexto(intencao, comando)
        pesquisar_no_google(params["termo"])

    elif intencao == "pesquisar_youtube":
        salvar_contexto(intencao, comando)
        pesquisar_no_youtube(params["termo"])

    elif intencao == "abrir_app":
        salvar_contexto(intencao, comando)
        abrir_aplicativo(params["app"])

    elif intencao == "aumentar_volume":
        salvar_contexto(intencao, comando)
        aumentar_volume()

    elif intencao == "diminuir_volume":
        salvar_contexto(intencao, comando)
        diminuir_volume()

    elif intencao == "mutar_volume":
        salvar_contexto(intencao, comando)
        mutar_volume()

    elif intencao == "alternar_play_pause":
        salvar_contexto(intencao, comando)
        alternar_play_pause()

    elif intencao == "proxima_musica":
        salvar_contexto(intencao, comando)
        proxima_musica()

    elif intencao == "musica_anterior":
        salvar_contexto(intencao, comando)
        musica_anterior()

    else:
        resposta = responder_conversa(comando)

        if resposta:
            salvar_contexto("conversa", comando)
            falar(resposta)
        else:
            resposta_ia = perguntar_ia_local(comando)

            if resposta_ia:
                salvar_contexto("ia_local", comando)
                falar(resposta_ia)
            else:
                falar_erro()