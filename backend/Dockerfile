FROM python:3.6
ENV PYTHONBUFFERED 1

RUN mkdir /backend
WORKDIR /backend

RUN apt-get update && apt-get upgrade -y && apt-get install -y libsqlite3-dev

RUN pip install -U pip setuptools

ADD . /backend/

EXPOSE 8000