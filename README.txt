Flask application that utilizies the Python slack_sdk. The application has a route called send_message that
will invoke a handler function that sends a message recieved by the client in JSON format to a designated
channel. After that I containerized that applicaion using a Dockerfile and then I created a Kubernetes deployment 
and Kubernetes service for the built Docker image. Then I deployed that service to a Kubernetes cluster.
I also created some unit tests for the service.