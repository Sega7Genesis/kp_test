from django.core.management.base import BaseCommand

from session_service.models import User


class Command(BaseCommand):
    help = "Count amount of items in database"

    def handle(self, *args, **options):
        self.stdout.write(str(User.objects.count()))
