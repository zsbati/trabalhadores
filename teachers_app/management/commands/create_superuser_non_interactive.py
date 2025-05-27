import os
import sys
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import IntegrityError

User = get_user_model()

class Command(BaseCommand):
    help = 'Creates a superuser non-interactively'

    def add_arguments(self, parser):
        parser.add_argument('--username', help='Superuser username')
        parser.add_argument('--email', help='Superuser email')
        parser.add_argument('--password', help='Superuser password')
        parser.add_argument('--noinput', '--no-input', action='store_false', 
                         dest='interactive',
                         help='Tells Django to NOT prompt the user for input of any kind.',)

    def handle(self, *args, **options):
        # Get values from command line arguments or environment variables
        username = options.get('username') or os.getenv('SUPERUSER_USERNAME')
        email = options.get('email') or os.getenv('SUPERUSER_EMAIL')
        password = options.get('password') or os.getenv('SUPERUSER_PASSWORD')
        
        # Set default values if not provided
        if not username:
            username = 'admin'
        if not email:
            email = f'{username}@example.com'
        if not password:
            self.stderr.write(
                self.style.ERROR('Error: You must provide a password via SUPERUSER_PASSWORD environment variable or --password argument')
            )
            sys.exit(1)

        try:
            # Check if user already exists
            if User.objects.filter(username=username).exists():
                self.stdout.write(self.style.WARNING(f'Superuser {username} already exists'))
                return

            # Create the superuser
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password,
                is_staff=True,
                is_superuser=True
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created superuser {username}'))
            
        except IntegrityError as e:
            self.stderr.write(self.style.ERROR(f'Error creating superuser: {str(e)}'))
            sys.exit(1)
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Unexpected error: {str(e)}'))
            sys.exit(1)
