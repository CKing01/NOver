import os
import sys

path = '/opt/render/project/src/'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'NOverBackend.settings'

# then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
