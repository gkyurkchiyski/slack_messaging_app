Flask-based web application that integrates with Slack using the python-slack-sdk. The application exposes 
a /send_message route that accepts JSON payloads from clients and forwards the message to a designated 
Slack channel through the Slack API.

The application was containerized using Docker, and a Kubernetes deployment and service were created 
to orchestrate and expose the application within a Kubernetes cluster. The service was successfully 
deployed and tested in the cluster environment.

To ensure reliability and correctness, I also implemented a set of unit tests to 
validate the message handling logic and Slack API interactions.

Key Technologies: Python, Flask, Slack SDK, Docker, Kubernetes (Deployment, Service), Unit Testing (pytest).
