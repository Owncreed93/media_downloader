from fastapi import APIRouter

from schemas.download import DownloadCreate, DownloadResponse
from api.controllers.download import create_download

router = APIRouter()

@router.post("/", response_model=DownloadResponse)
def add_download(download: DownloadCreate):
    return create_download(download.url, download.successful, download.media_type, download.created_at)