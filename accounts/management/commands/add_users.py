# accounts/management/commands/add_users.py
from django.core.management.base import BaseCommand
from accounts.models import User

class Command(BaseCommand):
    help = 'Creates default admin and doctor users'

    def handle(self, *args, **options):
        # Tworzenie użytkownika z rolą admin
        if not User.objects.filter(username='admin_user').exists():
            User.objects.create_user(
                username='admin_user',
                password='adminpassword',
                role='admin',
                is_staff=True,
                is_superuser=True
            )
            self.stdout.write(self.style.SUCCESS("Successfully created admin user"))

        # Tworzenie użytkownika z rolą doctor
        if not User.objects.filter(username='doctor_user').exists():
            User.objects.create_user(
                username='doctor_user',
                password='doctorpassword',
                role='doctor'
            )
            self.stdout.write(self.style.SUCCESS("Successfully created doctor user"))
