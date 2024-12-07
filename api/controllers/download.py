from datetime import datetime

from schemas.download import DownloadResponse
from youtbe_downloader.downloader import MediaDownloader
from utils.main import parse_date

def create_download(url: str, successful: bool, media_type: str, created_at: str) -> DownloadResponse:
    '''
    Creates a new download record
    '''
    # date = parse_date(created_at)
    if created_at:
        date = parse_date(created_at)
    else:
        date = datetime.date(datetime.now())
    media_type if media_type else 'video'
    downloader = MediaDownloader(url, media_type)
    if downloader.download():
        new_download = DownloadResponse(id=1, url=url, successful=successful, media_type=media_type, createdAt=date)
        print(downloader.metadata)
    else:
        new_download = None
    # return DownloadResponse(id=1, url=url, successful=successful)
    return new_download