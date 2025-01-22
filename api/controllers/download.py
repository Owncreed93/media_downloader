from datetime import datetime

from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from schemas.download import DownloadCreate, DownloadRequest, DownloadResponse
from youtbe_downloader.downloader import MediaDownloader
from utils.main import LOCAL_TZ
from api.query.download import save_download

def create_download(download_data: DownloadRequest, db: Session) -> DownloadResponse:
    '''
    Creates a new download record
    '''
    media_type = 'audio' if download_data.audio else 'video'

    downloader = MediaDownloader(download_data.url, media_type)

    try:
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
            download_obj = (DownloadResponse.from_sqlalchemy(new_download, download.media_type)).model_dump(mode='json')
            print(f'\n*****************\n {downloader.metadata} \n*****************\n')
            
            return JSONResponse(
                content={
                    'status': 'ok',
                    'download': download_obj,
                },
                status_code=200
            )
        else:
            return JSONResponse(
                content={
                    'status': 'Error',
                    'message': 'Failed to download media.'
                },
                status_code=400
            )
    except ValueError as ve:
        return JSONResponse(
            content={
                'status': 'Error',
                'message': str(ve),
            },
            status_code=400,
        )
    except Exception as e:
        print(str(e))
        return JSONResponse(
            content={
                'status': 'Error',
                'message': 'Contact system administrator.'
            },
            status_code=500
        )