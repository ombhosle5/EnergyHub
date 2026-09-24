"""
WSGI config for mission project.
"""

import os
import sys
from pathlib import Path

# Make sure the folder that holds "mission" and "app" is importable,
# even when Vercel runs from the outer repo folder.
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mission.settings')

application = get_wsgi_application()

# Vercel looks for a variable named "app"
app = application
