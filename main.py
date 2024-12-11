from fastapi import FastAPI

from api.routes.main import api_router
from db.base import init_db
#from youtbe_downloader.downloader import download_menu

app = FastAPI()

init_db()

@app.get('/')
def root():
    print('GAAA en el main')
    return {'message': 'Welcome to the Youtube Downloader API.'}


app.include_router(api_router, prefix='/api')