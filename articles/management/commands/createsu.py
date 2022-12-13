from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

class Command(BaseCommand):

    def handle(self, *args, **options):
        if not get_user_model().objects.filter(username="admin").exists():
            get_user_model().objects.create_superuser("admin", "admin@admin.com", "admin")
            self.stdout.write(self.style.SUCCESS('Successfully created new super user'))
