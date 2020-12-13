FROM python:3.7.5-slim

COPY grader /app/grader
COPY tests /app/tests
COPY grade.py /app/grade.py
COPY requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT pytest /app