from flask import Flask, request, jsonify
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os

app = Flask(__name__)

SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN", "xoxb-xxx")  # Safer for production
SLACK_CHANNEL = os.getenv("SLACK_CHANNEL", "#general")

client = WebClient(token=SLACK_APP_TOKEN)

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    message = data.get("message")

    if message:
        try:
            response = client.chat_postMessage(
                channel=SLACK_CHANNEL,
                text=message
            )
            return jsonify({"message": "Message sent successfully"})
        except SlackApiError as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "No message provided"}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0")