from fastapi import APIRouter

from api.routes.download import router as download_router

api_router = APIRouter()

api_router.include_router(download_router, prefix='/download', tags=['Downloads']) 