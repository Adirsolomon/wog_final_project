FROM selenium/standalone-chrome:latest

USER root

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-venv \
    iputils-ping \  
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*


RUN python3 -m venv /opt/venv

RUN /opt/venv/bin/pip install mysql-connector-python selenium

ENV PATH="/opt/venv/bin:$PATH"

USER seluser

WORKDIR /app

COPY tests.py .

CMD ["python", "tests.py"]




