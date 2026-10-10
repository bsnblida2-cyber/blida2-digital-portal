import os
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create the initial Django superuser from one-time deployment environment variables."

    def handle(self, *args, **options):
        username = os.environ.get("BOOTSTRAP_ADMIN_USERNAME", "").strip()
        email = os.environ.get("BOOTSTRAP_ADMIN_EMAIL", "").strip()
        password = os.environ.get("BOOTSTRAP_ADMIN_PASSWORD", "")

        if not any((username, email, password)):
            self.stdout.write("Initial admin bootstrap skipped (credentials not configured).")
            return
        if not all((username, email, password)):
            raise CommandError(
                "Set BOOTSTRAP_ADMIN_USERNAME, BOOTSTRAP_ADMIN_EMAIL and "
                "BOOTSTRAP_ADMIN_PASSWORD together, or remove all three."
            )
        if len(password) < 14:
            raise CommandError("BOOTSTRAP_ADMIN_PASSWORD must be at least 14 characters long.")

        User = get_user_model()
        existing = User._default_manager.filter(**{User.USERNAME_FIELD: username}).first()
        if existing:
            if not existing.is_superuser or not existing.is_staff:
                raise CommandError(
                    "The configured username already exists but is not a superuser. "
                    "Use a new username; existing accounts are never promoted automatically."
                )
            self.stdout.write(self.style.WARNING(
                "An admin with this username already exists; password and account were not changed."
            ))
            return

        user = User._default_manager.create_superuser(
            **{User.USERNAME_FIELD: username},
            email=email,
            password=password,
        )
        self.stdout.write(self.style.SUCCESS(f"Initial administrator created: {user.get_username()}"))
