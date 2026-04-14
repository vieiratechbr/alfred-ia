import re
from utils import normalizar_texto, tem_fragmento
from contexto import obter_ultima_intencao


INTENT_MAP = {
    "hora": {
        "palavras": ["hora", "horas"]
    },
    "data": {
        "palavras": ["data", "dia", "hoje"]
    },
    "internet": {
        "palavras": ["internet", "conexao", "conectado", "online"]
    },
    "bateria": {
        "palavras": ["bateria", "energia", "carga"]
    },
    "abrir_navegador": {
        "verbos": ["abra", "abre", "abrir", "abriu", "abrindo", "a brir", "abreira"],
        "alvos": ["navegador", "navega", "vivaldi", "browser"]
    },
    "abrir_apple_music": {
        "verbos": ["abra", "abre", "abrir", "abram", "abriu", "abrindo", "a brir"],
        "alvos": ["apple music", "music", "musica", "musica apple"]
    }
}


def detectar_intencao(texto):
    comando = normalizar_texto(texto)

    pesquisa_youtube = extrair_pesquisa_youtube(comando)
    if pesquisa_youtube:
        return {"intent": "pesquisar_youtube", "params": {"termo": pesquisa_youtube}}

    pesquisa_google = extrair_pesquisa_google(comando)
    if pesquisa_google:
        return {"intent": "pesquisar_google", "params": {"termo": pesquisa_google}}

    if entender_abrir_youtube(comando):
        return {"intent": "abrir_youtube", "params": {}}

    if entender_abrir_google(comando):
        return {"intent": "abrir_google", "params": {}}

    if any(p in comando for p in INTENT_MAP["hora"]["palavras"]):
        return {"intent": "hora", "params": {}}

    if any(p in comando for p in INTENT_MAP["data"]["palavras"]):
        return {"intent": "data", "params": {}}

    if any(p in comando for p in INTENT_MAP["internet"]["palavras"]):
        return {"intent": "internet", "params": {}}

    if any(p in comando for p in INTENT_MAP["bateria"]["palavras"]):
        return {"intent": "bateria", "params": {}}

    if tem_fragmento(comando, INTENT_MAP["abrir_navegador"]["verbos"]) and tem_fragmento(
        comando, INTENT_MAP["abrir_navegador"]["alvos"]
    ):
        return {"intent": "abrir_navegador", "params": {}}

    if tem_fragmento(comando, INTENT_MAP["abrir_apple_music"]["verbos"]) and tem_fragmento(
        comando, INTENT_MAP["abrir_apple_music"]["alvos"]
    ):
        return {"intent": "abrir_apple_music", "params": {}}

    intencao_contextual = detectar_intencao_contextual(comando)
    if intencao_contextual:
        return {"intent": intencao_contextual, "params": {}}

    return None


def entender_abrir_youtube(comando):
    return (
        ("youtube" in comando and any(v in comando for v in ["abra", "abre", "abrir"]))
        or "abra o navegador no youtube" in comando
        or "abra o youtube" in comando
    )


def entender_abrir_google(comando):
    return (
        ("google" in comando and any(v in comando for v in ["abra", "abre", "abrir"]))
        or "abra o navegador no google" in comando
        or "abra o google" in comando
    )


def extrair_pesquisa_youtube(comando):
    padroes = [
        r"pesquise por (.+?) no youtube",
        r"procure por (.+?) no youtube",
        r"busque por (.+?) no youtube",
        r"pesquisar por (.+?) no youtube"
    ]

    for padrao in padroes:
        match = re.search(padrao, comando)
        if match:
            return match.group(1).strip()

    return None


def extrair_pesquisa_google(comando):
    padroes = [
        r"pesquise por (.+)",
        r"procure por (.+)",
        r"busque por (.+)",
        r"pesquisar por (.+)"
    ]

    for padrao in padroes:
        match = re.search(padrao, comando)
        if match:
            termo = match.group(1).strip()
            if not termo.endswith("no youtube"):
                return termo

    return None


def detectar_intencao_contextual(comando):
    ultima_intencao = obter_ultima_intencao()

    if not ultima_intencao:
        return None

    if comando in ["e a data", "e data", "qual a data"]:
        return "data"

    if comando in ["e a hora", "e hora", "qual a hora"]:
        return "hora"

    if comando in ["e a bateria", "e bateria", "como ela esta"]:
        return "bateria"

    if comando in ["e a internet", "e internet", "tem conexao", "esta conectado"]:
        return "internet"

    if comando in ["e a musica", "e a musica agora", "abra a musica"]:
        return "abrir_apple_music"

    if comando in ["e o navegador", "abra o navegador", "abra o vivaldi"]:
        return "abrir_navegador"

    if ultima_intencao in ["hora", "data", "internet", "bateria"]:
        if comando in ["e agora", "e depois", "e tambem"]:
            return ultima_intencao

    return None