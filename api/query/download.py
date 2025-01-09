from sqlalchemy.orm import Session

from db.models.models import Download
from schemas.download import DownloadCreate

# def save_download(url: str, result: bool, media_type: str, created_at: datetime, db: Session = Depends(get_db)):
def save_download(db_download: DownloadCreate, db: Session):
    download = Download(youtube_url=db_download.url,
                        youtube_id=db_download.youtube_id,
                        title=db_download.title,
                        fulltitle=db_download.fulltitle,
                        uploader=db_download.uploader,
                        channel=db_download.channel,
                        duration=db_download.duration,
                        label=db_download.label,
                        copyright=db_download.copyright,
                        origin_url=db_download.origin_url,
                        live_status=db_download.live_status,
                        extractor=db_download.extractor,
                        categories=db_download.categories,
                        result=db_download.result,
                        created_at=db_download.created_at,
                        updated_at=db_download.created_at)
    try:
        db.add(download)
        db.commit()
        db.refresh(download)
    except Exception as e:
        print(f'Error: {e}')
        db.rollback()
        raise
    return download

