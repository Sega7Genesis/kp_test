#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
#python manage.py makemigrations equipment_service --no-input
python manage.py migrate equipment_service --no-input

echo "Collect static files"
python manage.py collectstatic --no-input


# Start server
echo "Starting server"
echo $SERVICE_PORT
gunicorn \
  --bind 0.0.0.0:$PORT \
  service.wsgi:application
