from datetime import datetime
import os
from pytz import timezone

BASE_DOWNLOAD_DIR = './downloads'
VIDEOS_DIR = BASE_DOWNLOAD_DIR+'/videos/'
AUDIOS_DIR = BASE_DOWNLOAD_DIR+'/audios/' 
BASE_YOUTUBE_URL = 'https://www.youtube.com/watch?v='
DATE_FORMAT = "%d/%m/%Y %H:%M:%S"
TIME_ZONE = 'America/Lima'
LOCAL_TZ = timezone(TIME_ZONE)
# VIDEO_ID = 'ANItN-hBrC0'


def create_directories(path: str):
    os.makedirs(path, exist_ok=True)

def format_date(date: datetime, tz: str = 'America/Lima') -> str:
    """Converts a date to format dd/mm/yyyy"""
    if not date:
        date = None
    local_tz = timezone(tz)
    localized_date = date.astimezone(local_tz)
    return localized_date.strftime(DATE_FORMAT)

def parse_date(date_str: str, tz: str = 'America/Lima') -> datetime:
    """Converts a string in dd/mm/yyyy format to a datatime object"""
    if not date_str:
        date = None
    local_tz = timezone(tz)
    native_date = datetime.strptime(date_str, DATE_FORMAT)
    localized_date = local_tz.localize(native_date)
    return localized_date