FROM python:3

LABEL org.opencontainers.image.authors="Epitech TOULOUSE"
LABEL multi.label1="By Anthony and Léo" \
      multi.label2="For Projet hub des association"

ENV PYTHONUNBUFFERED 1

RUN mkdir /backend
WORKDIR /backend
COPY . /backend/

RUN pip install -r requirements.txt