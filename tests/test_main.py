from fastapi.testclient import TestClient
from heroapi_auit.main import app

def test_root_path():
    client:TestClient = TestClient(app=app)
    response = client.get('/')
    assert response.status_code == 200