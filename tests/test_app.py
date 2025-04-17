import pytest
from slack_messaging_app.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_send_message_success(client, monkeypatch):
    # Mock Slack API call
    def mock_post_message(**kwargs):
        class MockResponse:
            data = {"ok": True}
        return MockResponse()
    
    from slack_messaging_app import app as app_module
    app_module.client.chat_postMessage = mock_post_message

    response = client.post("/send_message", json={"message": "Hello Slack!"})
    assert response.status_code == 200
    assert response.get_json() == {"message": "Message sent successfully"}

def test_send_message_missing_message(client):
    response = client.post("/send_message", json={})
    assert response.status_code == 400
    assert response.get_json() == {"error": "No message provided"}