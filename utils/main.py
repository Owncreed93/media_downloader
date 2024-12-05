import os

BASE_DOWNLOAD_DIR = './downloads'
VIDEOS_DIR = BASE_DOWNLOAD_DIR+'/videos/'
AUDIOS_DIR = BASE_DOWNLOAD_DIR+'/audios/' 
BASE_YOUTUBE_URL = 'https://www.youtube.com/watch?v='
# VIDEO_ID = 'ANItN-hBrC0'

def create_directories():
    os.makedirs(VIDEOS_DIR, exist_ok=True)
    os.makedirs(AUDIOS_DIR, exist_ok=True)