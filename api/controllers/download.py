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
        new_download = save_download(download_data, db)
        #new_download = DownloadResponse(id=1, url=url, result=result, media_type=media_type, createdAt=date)
        response = DownloadResponse.from_sqlalchemy(new_download, download_data.media_type)
        print(downloader.metadata)
        # return DownloadResponse(id=1, url=url, result=result)
        return response
    else:
        raise ValueError("Failed to download media.")
    