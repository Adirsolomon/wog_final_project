# Use the official Selenium base image with Chrome and ChromeDriver pre-installed
FROM selenium/standalone-chrome:latest

# Switch to root to install utilities
USER root

# Install Python, pip, and ping utility
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-venv \
    iputils-ping \  
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Create a virtual environment
RUN python3 -m venv /opt/venv

# Activate the virtual environment and install Python dependencies
RUN /opt/venv/bin/pip install mysql-connector-python selenium

# Set environment variables to use the virtual environment
ENV PATH="/opt/venv/bin:$PATH"

# Switch back to non-root user
USER seluser

# Set up working directory
WORKDIR /app

# Copy the test script into the container
COPY tests.py .




