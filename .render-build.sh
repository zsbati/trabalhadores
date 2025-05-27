#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Create superuser if it doesn't exist
python manage.py create_superuser_non_interactive \
    --username="${SUPERUSER_USERNAME:-admin}" \
    --email="${SUPERUSER_EMAIL:-admin@example.com}" \
    --password="${SUPERUSER_PASSWORD}" || true

# Collect static files (after migrations to ensure all apps are ready)
python manage.py collectstatic --noinput
