#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install Python dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create database directory if it doesn't exist
DB_DIR=$(python -c "import os; from pathlib import Path; print(Path(os.getcwd()) / 'db.sqlite3')")
echo "Database path: $DB_DIR"
mkdir -p "$(dirname "$DB_DIR")"

# Apply database migrations
echo "Applying migrations..."
python manage.py makemigrations
echo "Running migrations..."
python manage.py migrate --noinput

# Create superuser if it doesn't exist
echo "Creating superuser..."
python manage.py shell -c "
import os
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username=os.getenv('SUPERUSER_USERNAME', 'admin')).exists():
    User.objects.create_superuser(
        username=os.getenv('SUPERUSER_USERNAME', 'admin'),
        email=os.getenv('SUPERUSER_EMAIL', 'admin@example.com'),
        password=os.getenv('SUPERUSER_PASSWORD', 'adminpass123')
    )
    print('Superuser created successfully')
else:
    print('Superuser already exists')
"

# Set up static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Build completed successfully!"
