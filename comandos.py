import re
import unicodedata

from acoes import (
    abrir_navegador,
    abrir_apple_music,
    dizer_hora,
    dizer_data,
    verificar_internet,
    mostrar_bateria
)

from speaker import falar_erro


def normalizar_texto(texto):
    texto = texto.lower().strip()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    texto = re.sub(r"[^a-z0-9\s]", " ", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto


def tem_fragmento(texto, fragmentos):
    return any(fragmento in texto for fragmento in fragmentos)


def entender_comando_hora(comando):
    palavras = ["hora", "horas"]
    return any(p in comando for p in palavras)


def entender_comando_data(comando):
    palavras = ["data", "dia", "hoje"]
    return any(p in comando for p in palavras)


def entender_comando_internet(comando):
    palavras = ["internet", "conexao", "conectado", "online"]
    return any(p in comando for p in palavras)


def entender_comando_bateria(comando):
    palavras = ["bateria", "energia", "carga"]
    return any(p in comando for p in palavras)


def entender_comando_navegador(comando):
    verbos = ["abra", "abre", "abrir", "abriu", "abrindo", "a brir", "abreira"]
    alvos = ["navegador", "navega", "vivaldi", "browser"]
    return tem_fragmento(comando, verbos) and tem_fragmento(comando, alvos)


def entender_comando_apple_music(comando):
    verbos = ["abra", "abre", "abrir", "abram", "abriu", "abrindo", "a brir"]
    alvos = ["apple music", "music", "musica", "musica apple"]
    return tem_fragmento(comando, verbos) and tem_fragmento(comando, alvos)


def executar_comando(comando):
    comando_original = comando
    comando = normalizar_texto(comando)

    if entender_comando_hora(comando):
        dizer_hora()

    elif entender_comando_data(comando):
        dizer_data()

    elif entender_comando_internet(comando):
        verificar_internet()

    elif entender_comando_bateria(comando):
        mostrar_bateria()

    elif entender_comando_navegador(comando):
        abrir_navegador()

    elif entender_comando_apple_music(comando):
        abrir_apple_music()

    else:
        print(f"Alfred: comando não reconhecido -> {comando_original}")
        falar_erro()