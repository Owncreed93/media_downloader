from datetime import datetime
from sqlalchemy.orm import Session

from schemas.download import DownloadCreate, DownloadRequest, DownloadResponse
from youtbe_downloader.downloader import MediaDownloader
from utils.main import parse_date, LOCAL_TZ
from api.query.download import save_download

# def create_download(url: str, media_type: str, created_at: str) -> DownloadResponse:
def create_download(download_data: DownloadRequest, db: Session) -> DownloadResponse:
    '''
    Creates a new download record
    '''
    media_type = 'audio' if download_data.audio else 'video'

    downloader = MediaDownloader(download_data.url, media_type)

    if downloader.download():
        download = DownloadCreate(
            url=download_data.url,
            youtube_id = downloader.metadata.get('youtube_id'),
            title=downloader.metadata.get('title'),
            fulltitle=downloader.metadata.get('fulltitle'),
            uploader=downloader.metadata.get('uploader'),
            channel=downloader.metadata.get('channel'),
            duration=downloader.metadata.get('duration'),
            label=downloader.metadata.get('label'),
            copyright=downloader.metadata.get('copyright'),
            origin_url=downloader.metadata.get('origin_url'),
            live_status=downloader.metadata.get('live_status'),
            extractor=downloader.metadata.get('extractor'),
            categories=downloader.metadata.get('categories'),
            result=True,
            media_type=media_type,
            created_at=datetime.now(LOCAL_TZ)
        )

        new_download = save_download(download, db)
        response = DownloadResponse.from_sqlalchemy(new_download, download.media_type)
        print(f'\n*****************\n {downloader.metadata} \n*****************\n')
        return response
    else:
        raise ValueError("Failed to download media.")
    