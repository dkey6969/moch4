"""
WSGI config for main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
    application = get_wsgi_application()
except Exception as e:
    # Логирование ошибки
    sys.stderr.write(f"WSGI error: {e}\n")
    raise
