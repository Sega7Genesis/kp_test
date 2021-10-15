#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate generator_service --no-input

echo "Collect static files"
python manage.py collectstatic --no-input


# Start server
echo "Starting server"
gunicorn \
  --bind 0.0.0.0:$PORT \
  service.wsgi:application
