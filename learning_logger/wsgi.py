"""
WSGI config for learning_logger project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling #cling helps serve static files and used to launch the app

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_logger.settings')

application = Cling(get_wsgi_application())
