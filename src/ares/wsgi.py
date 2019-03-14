"""
WSGI config for ares project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

try:
    import pymysql
    pymysql.install_as_MySQLdb()
except Exception as e:
    pass

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ares.settings")

application = get_wsgi_application()
