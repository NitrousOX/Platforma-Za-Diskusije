# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy dependencies and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set Flask environment to development to enable debug mode
ENV FLASK_ENV=development

# Expose the API port
EXPOSE 5000

# Run the Flask application using the built-in server
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
