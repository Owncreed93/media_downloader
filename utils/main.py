from datetime import datetime
import os

BASE_DOWNLOAD_DIR = './downloads'
VIDEOS_DIR = BASE_DOWNLOAD_DIR+'/videos/'
AUDIOS_DIR = BASE_DOWNLOAD_DIR+'/audios/' 
BASE_YOUTUBE_URL = 'https://www.youtube.com/watch?v='
DATE_FORMAT = "%d/%m/%Y"
# VIDEO_ID = 'ANItN-hBrC0'


def create_directories(path: str):
    os.makedirs(path, exist_ok=True)

def format_date(date: datetime) -> str:
    """Converts a date to format dd/mm/yyyy"""
    return date.strftime(DATE_FORMAT) if date else None

def parse_date(date_str: str) -> datetime:
    """Converts a string in dd/mm/yyyy format to a datatime object"""
    return datetime.strptime(date_str, DATE_FORMAT) if date_str else None