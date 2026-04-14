contexto_atual = {
    "ultima_intencao": None,
    "ultimo_comando": None
}


def salvar_contexto(intencao, comando):
    contexto_atual["ultima_intencao"] = intencao
    contexto_atual["ultimo_comando"] = comando


def obter_ultima_intencao():
    return contexto_atual["ultima_intencao"]


def obter_ultimo_comando():
    return contexto_atual["ultimo_comando"]