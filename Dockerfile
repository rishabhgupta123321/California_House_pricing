# This is our base Dockerfile for deploying a Flask app on Render.com

# Use Python 3.13 slim image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project
COPY . .

# Optional (Render ignores this, but nice for docs)
EXPOSE 8000

# Start Flask app with Gunicorn (Render sets $PORT automatically)
CMD gunicorn --bind 0.0.0.0:$PORT app:app


  