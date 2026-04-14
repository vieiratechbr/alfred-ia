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

    if any(p in comando for p in INTENT_MAP["hora"]["palavras"]):
        return "hora"

    if any(p in comando for p in INTENT_MAP["data"]["palavras"]):
        return "data"

    if any(p in comando for p in INTENT_MAP["internet"]["palavras"]):
        return "internet"

    if any(p in comando for p in INTENT_MAP["bateria"]["palavras"]):
        return "bateria"

    if tem_fragmento(comando, INTENT_MAP["abrir_navegador"]["verbos"]) and tem_fragmento(
        comando, INTENT_MAP["abrir_navegador"]["alvos"]
    ):
        return "abrir_navegador"

    if tem_fragmento(comando, INTENT_MAP["abrir_apple_music"]["verbos"]) and tem_fragmento(
        comando, INTENT_MAP["abrir_apple_music"]["alvos"]
    ):
        return "abrir_apple_music"

    intencao_contextual = detectar_intencao_contextual(comando)
    if intencao_contextual:
        return intencao_contextual

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