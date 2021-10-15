#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate report_service --no-input

echo "Collect static files"
python manage.py collectstatic --no-input


# Start server
echo "Starting server"
gunicorn \
  --bind 0.0.0.0:$SERVICE_PORT \
  service.wsgi:application
