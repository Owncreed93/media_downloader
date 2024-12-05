from yt_dlp import YoutubeDL


from utils.main import (create_directories,
                        VIDEOS_DIR,
                        AUDIOS_DIR,
                        BASE_YOUTUBE_URL)

# Función para descargar un video
def descargar_video(video_id, directorio=VIDEOS_DIR):
    url = BASE_YOUTUBE_URL+video_id
    print(f"Iniciando descarga de video: {url}")
    opciones = {
        'format': 'bestvideo[height<=1440]+bestaudio/best[ext=mp4]/best',
        'outtmpl': f'{directorio}%(title)s.%(ext)s',
        'progress_hooks': [progreso_descarga],
        'postprocessors': [{'key': 'FFmpegMetadata'}],
    }
    try:
        with YoutubeDL(opciones) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"Error al descargar el video: {e}")

# Función para descargar un audio
def descargar_audio(video_id, directorio=AUDIOS_DIR):
    url = BASE_YOUTUBE_URL+video_id
    print(f"Iniciando descarga de audio: {url}")
    opciones = {
        'format': 'bestaudio/best',
        'outtmpl': f'{directorio}%(title)s.%(ext)s',
        'progress_hooks': [progreso_descarga],
        'postprocessors': [
            {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'},
            {'key': 'FFmpegMetadata'},
        ],
    }
    try:
        with YoutubeDL(opciones) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"Error al descargar el audio: {e}")

# Hook para mostrar progreso de descarga
def progreso_descarga(d):
    if d['status'] == 'downloading':
        print(f"Descargando: {d['_percent_str']} completado - {d['_eta_str']} restantes")
    elif d['status'] == 'finished':
        print("Descarga completada correctamente.")
    elif d['status'] == 'error':
        print("Ocurrió un error durante la descarga.")

# Función para procesar una lista de URLs desde un archivo
def procesar_lista(archivo, tipo="video"):
    try:
        with open(archivo, 'r') as f:
            urls = f.read().splitlines()
        for url in urls:
            if tipo == "video":
                descargar_video(url)
            elif tipo == "audio":
                descargar_audio(url)
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe.")
    except Exception as e:
        print(f"Error al procesar la lista: {e}")

# Interfaz principal
def download_menu():
    create_directories()
    print("Bienvenido al descargador de YouTube.")
    print("Opciones disponibles:")
    print("1. Descargar video")
    print("2. Descargar audio")

    opcion = input("Selecciona una opción (1 o 2): ")
    entrada = input("Proporciona una URL o el archivo con URLs (terminación .txt): ")

    if entrada.endswith('.txt'):
        tipo = "video" if opcion == "1" else "audio"
        procesar_lista(entrada, tipo=tipo)
    else:
        if opcion == "1":
            descargar_video(entrada)
        elif opcion == "2":
            descargar_audio(entrada)
        else:
            print("Opción inválida. Selecciona 1 o 2.")