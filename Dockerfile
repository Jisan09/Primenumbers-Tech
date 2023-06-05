FROM debian:bullseye-slim

# Update packages and install dependencies
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -fy --no-install-recommends \
        chromium \
        chromium-driver \
        gcc \
        python3 \
        python3-pip

## Copy files into the Docker image
COPY . .

# Upgrade pip and install Python packages
RUN pip3 install --upgrade pip setuptools && \
    pip3 install --no-cache-dir -r requirements.txt

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONWARNINGS=ignore \
    CHROME_BIN=/usr/bin/chromium \
    CHROME_DRIVER=/usr/bin/chromedriver

# Set default command
CMD ["python3","./scrapper.py"]