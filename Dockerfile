# Use an amd64-compatible base image
FROM python:3.10.9-bullseye

# Set working directory
WORKDIR /app

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY slack_messaging_app/ /app/slack_messaging_app/

# Set environment variable (correct format)
ENV FLASK_APP=slack_messaging_app.app

# Expose port
EXPOSE 5000

# Run the Flask app
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]