FROM python:3.11.2-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /site

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .