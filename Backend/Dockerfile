# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy dependencies and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose the API port
EXPOSE 5000

# Run the application using Gunicorn with WebSocket support
CMD ["gunicorn", "-k", "eventlet", "-b", "0.0.0.0:5000", "run:app"]
