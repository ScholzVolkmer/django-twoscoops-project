import os
import sys
sys.stdout = sys.stderr


prev_sys_path = list(sys.path)

# Add the virtual Python environment site-packages directory to the path
import site
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))
site_packages_path = os.path.join(PROJECT_DIR, 'virtualenv/lib/python2.7/site-packages')
django_project_path = os.path.join(PROJECT_DIR, '{{project_name}}')
site.addsitedir(site_packages_path)
site.addsitedir(django_project_path)

new_sys_path = []
for item in list(sys.path):
    if item not in prev_sys_path:
        new_sys_path.append(item)
        sys.path.remove(item)
sys.path[:0] = new_sys_path

os.environ["APP_SETTINGS"] = "development"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{project_name}}.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
