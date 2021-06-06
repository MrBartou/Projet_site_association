# UwU
FROM python:3.9-slim

ENV PYTHONUNBUFFERED=True DEBIAN_FRONTEND=noninteractive PYTHONDONTWRITEBYTECODE=True

WORKDIR /usr/src/app
EXPOSE 8000/tcp

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python", "manage.py" ]
CMD [ "runserver", "0.0.0.0:8000" ]
