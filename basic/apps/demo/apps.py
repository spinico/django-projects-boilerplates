import sys

from django.apps import AppConfig


class DemoConfig(AppConfig):
    name = 'demo'
    verbose_name = 'Demo Application'

    def ready(self):
        # Only run this with "runserver" or "runserver_plus" and not when making migrations, migrate, shell, etc.
        if 'runserver' not in sys.argv and 'runserver_plus' not in sys.argv:
            return True

        # Import modules here to avoid AppRegistryNotReady exception
        # from .models import MyModel

        # Startup code here
