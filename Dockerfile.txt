# Use a lightweight Python base image
FROM python:3.10-slim

# Install system dependencies (ffmpeg is installed as an example)
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Upgrade pip to the latest version
RUN pip install --no-cache-dir --upgrade pip

# Optionally set the working directory (this is good practice for later additions)
WORKDIR /app

# Expose port 8080 for future use
EXPOSE 8080

# Placeholder command to keep the container running without an app entrypoint
CMD ["tail", "-f", "/dev/null"]
