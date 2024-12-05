from fastapi.testclient import TestClient
from main import app

cliente = TestClient(app)

def test_root():
    response = cliente.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Welcome to the Youtube Downloader API.'} 