from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.download import DownloadRequest, DownloadResponse
from api.controllers.download import create_download
from api.query.db_connection import get_db

router = APIRouter()

@router.post("/", response_model=DownloadResponse)
def add_download(download_data: DownloadRequest, db: Session = Depends(get_db)):
    # return create_download(download.url, download.media_type, download.created_at)
    return create_download(download_data, db)