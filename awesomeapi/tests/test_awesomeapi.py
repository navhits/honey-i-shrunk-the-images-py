# pylint: disable=all
from awesomeapi import __version__
from awesomeapi.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_version():
    assert __version__ == '0.1.0'

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello"}

def test_path_param():
    value = "test_case_value"
    response = client.get(f"/path/{value}")
    assert response.status_code == 200
    assert response.json() == {"message": value}

def test_query_param():
    value = "test_case_value"
    response = client.get(f"/query?query_param={value}")
    assert response.status_code == 200
    assert response.json() == {"message": value}
    