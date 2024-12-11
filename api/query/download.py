from sqlalchemy.orm import Session

from db.models.models import Download
from schemas.download import DownloadCreate

# def save_download(url: str, result: bool, media_type: str, created_at: datetime, db: Session = Depends(get_db)):
def save_download(db_download: DownloadCreate, db: Session):
    download = Download(youtube_url=db_download.url,
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

