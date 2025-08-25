from fastapi.testclient import TestClient
from unittest.mock import patch
import app

client = TestClient(app.app)  # app.app because in app.py: app = FastAPI()

@patch("app.requests.get")
def test_get_weather_success(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "location": {"name": "London"},
        "current": {"temp_c": 20, "condition": {"text": "Sunny"}}
    }

    response = client.get("/weather/London")
    assert response.status_code == 200
    assert response.json() == {
        "city": "London",
        "temperature": 20,
        "description": "Sunny"
    }

@patch("app.requests.get")
def test_get_weather_fail(mock_get):
    mock_get.return_value.status_code = 404
    mock_get.return_value.json.return_value = {}

    response = client.get("/weather/UnknownCity")
    assert response.status_code == 200
    assert response.json() == {"error": "City not found or API error"}