FROM python:3.7.5-slim

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT pytest tests