from unittest.mock import patch
import cli_app

@patch("cli_app.requests.get")
def test_cli_get_weather_success(mock_get, capsys):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "current": {
            "condition": {"text": "Sunny"},
            "temp_c": 20,
            "wind_kph": 15
        }
    }

    cli_app.get_weather("London", "fake_key")
    captured = capsys.readouterr()
    assert "Weather in London:" in captured.out
    assert "Sunny" in captured.out
    assert "20 °C" in captured.out
    assert "15 Km/hr" in captured.out

@patch("cli_app.requests.get")
def test_cli_get_weather_fail(mock_get, capsys):
    mock_get.return_value.status_code = 404

    cli_app.get_weather("UnknownCity", "fake_key")
    captured = capsys.readouterr()
    assert "unknowncity Not Found" in captured.out
