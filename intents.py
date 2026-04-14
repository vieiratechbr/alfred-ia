from utils import normalizar_texto, tem_fragmento


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

    return None