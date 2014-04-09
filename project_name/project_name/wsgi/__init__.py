"""
This WSGI is supposed to use the default settings and the default runserver.
DO NOT USE IT FOR ANYTHING ELSE
"""
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{project_name}}.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
