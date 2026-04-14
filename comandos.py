import re
import unicodedata
from acoes import abrir_navegador, abrir_apple_music


def normalizar_texto(texto):
    texto = texto.lower().strip()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    texto = re.sub(r"[^a-z0-9\s]", " ", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto


def tem_fragmento(texto, fragmentos):
    return any(fragmento in texto for fragmento in fragmentos)


def entender_comando_navegador(comando):
    verbos = [
        "abra", "abre", "abrir", "abriu", "abrindo",
        "a brir", "abreira"
    ]
    alvos = [
        "navegador", "navega", "vivaldi", "browser"
    ]

    return tem_fragmento(comando, verbos) and tem_fragmento(comando, alvos)


def entender_comando_apple_music(comando):
    verbos = [
        "abra", "abre", "abrir", "abram", "abriu", "abrindo",
        "a brir"
    ]
    alvos = [
        "apple music", "music", "musica", "musica apple"
    ]

    return tem_fragmento(comando, verbos) and tem_fragmento(comando, alvos)


def executar_comando(comando):
    comando_original = comando
    comando = normalizar_texto(comando)

    if entender_comando_navegador(comando):
        abrir_navegador()

    elif entender_comando_apple_music(comando):
        abrir_apple_music()

    else:
        print(f"Alfred: comando não reconhecido -> {comando_original}")