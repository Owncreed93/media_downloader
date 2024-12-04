import yt_dlp

def descargar_video(url, salida="./downloads/"):
    opciones = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': f'{salida}%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])

video_id = 'tk8ZKe_Sw2U'
# Llama la función con una URL de YouTube
descargar_video(f"https://www.youtube.com/watch?v={video_id}")