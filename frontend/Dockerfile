FROM node:latest

LABEL org.opencontainers.image.authors="Epitech TOULOUSE"
LABEL multi.label1="By Anthony and Léo" \
      multi.label2="For Projet hub des association"

RUN mkdir -p /app

WORKDIR /app

COPY package*.json /app/

RUN npm install

COPY . /app/

EXPOSE 4200

CMD [ "npm", "start"]