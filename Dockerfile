# Dockerfile --> For assignment simulation
# Use a lightweight Python 3.11 image to match your local environment
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first (better layer caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose port 8000
EXPOSE 8000

# Run the app
CMD ["python", "main.py"]
 
