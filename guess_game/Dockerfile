FROM python:3.9-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        libc-dev \
        default-libmysqlclient-dev \
        build-essential \
        pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . . 

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]