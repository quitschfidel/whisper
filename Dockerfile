# Use a lightweight Python base image
FROM python:3.10-slim

# Install system dependencies (e.g., ffmpeg, which Whisper requires)
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip to the latest version
RUN pip install --no-cache-dir --upgrade pip

# Install Python dependencies: Flask for the web server, and Whisper from your GitHub fork
RUN pip install --no-cache-dir flask && \
    pip install --no-cache-dir git+https://github.com/quitschfidel/whisper.git

# Set the working directory inside the container (good practice)
WORKDIR /app

# Copy all files from your repository into the container's working directory
COPY . .

# Expose port 8080 so the container will listen for web requests on that port
EXPOSE 8080

# Run your application using app.py
CMD ["python", "app.py"]

