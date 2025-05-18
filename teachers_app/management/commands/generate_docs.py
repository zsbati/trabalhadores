from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from django.utils import timezone
import os

class Command(BaseCommand):
    help = 'Generates documentation files from templates'

    def handle(self, *args, **options):
        # Get the base directory
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        docs_dir = os.path.join(base_dir, 'docs')
        
        # Create docs directory if it doesn't exist
        os.makedirs(docs_dir, exist_ok=True)
        
        # Generate API documentation
        api_docs = render_to_string('docs/api_docs.md', {
            'last_updated': timezone.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        
        # Save API documentation
        with open(os.path.join(docs_dir, 'api.md'), 'w', encoding='utf-8') as f:
            f.write(api_docs)
        
        # Generate admin guide
        admin_docs = render_to_string('docs/admin_guide.md', {
            'last_updated': timezone.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        
        # Save admin guide
        with open(os.path.join(docs_dir, 'admin_guide.md'), 'w', encoding='utf-8') as f:
            f.write(admin_docs)
        
        self.stdout.write(self.style.SUCCESS('Successfully generated documentation'))
