#!/usr/bin/env bash

pdoc --html backend/backend

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver