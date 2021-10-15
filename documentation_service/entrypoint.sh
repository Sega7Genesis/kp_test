#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate documentation_service --no-input


# Start server
echo "Starting server"
gunicorn \
  --bind 0.0.0.0:$PORT \
  service.wsgi:application
