#!/bin/bash

# Start Django server
python manage.py runserver 0.0.0.0:8000 &

# Start Celery worker
celery -A gateway worker -l info &

# Start Celery beat
celery -A gateway beat -l info &

