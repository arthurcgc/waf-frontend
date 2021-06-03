# syntax=docker/dockerfile:1

FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

RUN ls

ENTRYPOINT [ "gunicorn", "main:app", "-w", "2", "--threads", "2", "-b", "0.0.0.0:8000" ]
