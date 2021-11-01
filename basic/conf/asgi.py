"""
ASGI config for conf project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

settings = os.environ.get('DJANGO_SETTINGS_MODULE')

if not (settings and settings.strip()):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.production')
    settings = os.environ.get('DJANGO_SETTINGS_MODULE')

application = get_asgi_application()
