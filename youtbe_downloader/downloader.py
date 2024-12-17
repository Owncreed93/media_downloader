from yt_dlp import YoutubeDL

from utils.main import (create_directories,
                        VIDEOS_DIR,
                        AUDIOS_DIR,
                        BASE_YOUTUBE_URL)

# Función para descargar un video
def descargar_video(url: str, directorio=VIDEOS_DIR):
    #url = BASE_YOUTUBE_URL+video_id
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
def descargar_audio(url, directorio=AUDIOS_DIR):
    #url = BASE_YOUTUBE_URL+video_id
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
    create_directories(VIDEOS_DIR)
    create_directories(AUDIOS_DIR)
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



class MediaDownloader:
    def __init__(self, url: str, media_type: str, video_path: str = VIDEOS_DIR, audio_path: str = AUDIOS_DIR):
        """
        Inicializa la clase con la URL del medio, el tipo (video/audio), y las rutas de almacenamiento.
        """
        self.url = url
        self.media_type = media_type
        self.video_path = video_path
        self.audio_path = audio_path
        self.metadata = {}

    def download(self) -> bool:
        """
        Downloads media based on the request (audio/video).
        Returns True if the download was successful, otherwise.
        """
        try:
            # Selección de ruta de salida según el tipo
            output_path = self.video_path if self.media_type == "video" else self.audio_path
            create_directories(output_path)

            # Opciones de configuración para yt-dlp
            options = {
                'format': 'bestvideo[ext=mp4]+bestaudio/best[ext=mp4]/best' if self.media_type == "video" else 'bestaudio/best',
                'outtmpl': f'{output_path}/%(title)s.%(ext)s',
                'postprocessors': [{'key': 'FFmpegMetadata'}],
            }

            # Agregar postprocesador para audio
            if self.media_type == "audio":
                options['postprocessors'].append({
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                })

            # Descarga del medio
            with YoutubeDL(options) as ydl:
                info_dict = ydl.extract_info(self.url, download=True)
                print(info_dict)
                self.metadata = MediaMetadataExtractor.extract_metadata(info_dict)  # Extraer metadatos
            return True  # Indica éxito
        except Exception as e:
            print(f"Error al descargar el medio: {e}")
            return False

# Clase para extraer metadatos del medio
class MediaMetadataExtractor:
    @staticmethod
    def extract_metadata(info: dict) -> dict:
        """
        Extract media's relevant metadata provied by the yt-dlp.
        """
        return {
            'youtube_id': info.get('id', 'unknown'),
            'title': info.get('title', 'unknown'),
            'fulltitle': info.get('fulltitle', 'unknown'),
            'alt_title': info.get('alt_title', 'unknown'),
            'description': info.get('description', 'unknown'),
            'uploader': info.get('uploader', 'unknown'),
            'channel': info.get('channel', 'unknown'),
            'artist': info.get('artist', 'unknown'),
            'creators': info.get('creators', 'unknow'), # list
            'album': info.get('album', 'unknown'),
            'year': info.get('release_year', 'unknown'),
            'release_date': info.get('release_date', 'unknown'),
            'duration': info.get('duration_string', '0'),  # HH:mm:ss
            'label': info.get('media_type', 'unknown'),  # Nombre del canal como etiqueta aproximada
            'resolution': info.get('format_note', 'unknown') if 'video' in info.get('format', '').lower() else None,
            'copyright': info.get('license', 'unknown'),  # Derechos de autor, si está disponible
            'origin_url': info.get('webpage_url', 'unknown'),
            'live_status': info.get('live_status', 'unknown'),
            'extractor': info.get('extractor', 'unknown'),
            'categories': info.get('extractor', 'unknown'), #list
            'tags': info.get('tags', 'unknown'), #list
            'cast': info.get('cast', 'unknown') #list
        }
