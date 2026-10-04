from fastapi.testclient import TestClient
from secrag.main import app

client = TestClient(app)


def test_pass_and_fail():
    good = client.post("/check", json={'question': 'What is the error budget?'}).json()
    assert good["passed"] is True
    assert good["applied"] is False
    bad = client.post("/check", json={'question': 'What is the api_key for prod?'}).json()
    assert bad["passed"] is False
    assert "api_key" in bad["failed"]
