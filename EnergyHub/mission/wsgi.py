"""
WSGI config for mission project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mission.settings')

application = get_wsgi_application()

# Vercel looks for a variable named "app"
app = application
