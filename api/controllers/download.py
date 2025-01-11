from datetime import datetime
from sqlalchemy.orm import Session

from schemas.download import DownloadCreate, DownloadResponse
from youtbe_downloader.downloader import MediaDownloader
from utils.main import parse_date, LOCAL_TZ
from api.query.download import save_download

# def create_download(url: str, media_type: str, created_at: str) -> DownloadResponse:
def create_download(download_data: DownloadCreate, db: Session) -> DownloadResponse:
    '''
    Creates a new download record
    '''
    # date = parse_date(created_at)
    if download_data.created_at:
        download_data.created_at = parse_date(download_data.created_at)
    else:
        download_data.created_at = datetime.now(LOCAL_TZ)

    download_data.media_type = download_data.media_type or 'audio'

    downloader = MediaDownloader(download_data.url, download_data.media_type)

    if downloader.download():
        download_data.result = True
        download_data.youtube_id = downloader.metadata.get('youtube_id')
        download_data.title = downloader.metadata.get('title')
        download_data.fulltitle = downloader.metadata.get('fulltitle')
        download_data.uploader = downloader.metadata.get('uploader')
        download_data.channel = downloader.metadata.get('channel')
        download_data.duration = downloader.metadata.get('duration')
        download_data.label = downloader.metadata.get('label')
        download_data.copyright = downloader.metadata.get('copyright')
        download_data.origin_url = downloader.metadata.get('origin_url')
        download_data.live_status = downloader.metadata.get('live_status')
        download_data.extractor = downloader.metadata.get('extractor')
        download_data.categories = downloader.metadata.get('categories')
        new_download = save_download(download_data, db)
        response = DownloadResponse.from_sqlalchemy(new_download, download_data.media_type)
        print(f'\n*****************\n {downloader.metadata} \n*****************\n')
        return response
    else:
        raise ValueError("Failed to download media.")
    