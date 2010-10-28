#!/usr/bin/env python

import sys, os

project_name = os.path.basename(os.getenv("VIRTUAL_ENV"))

# try:
#   exec "from %s.config import settings" % project_name
# except ImportError:
#   from django.conf import settings

def get_var(var_name, default=''):
    val = getattr(settings, var_name, default)
    print val
    
def get_path(var_name):
    val = get_var(var_name, [])
    val = ":".join(val)
    print val

if __name__ == '__main__':
    
    setting_missing = True
    
    try:
        sys.path.insert(0, os.path.dirname(__file__))
        settings = __import__('django_env_settings', globals(), locals(), [])
        del sys.path[0]
    except ImportError:
        raise Exception("\n\n\
Error: The django_env_settings.py file is missing.\n\n\
You need to add the file %s/django_env_settings.py and include the following django-environment settings.\n\n\
DJANGO_ENV_PROJECT_DIR     = '/path/to/your/django/project/root'\n\
DJANGO_ENV_SETTINGS_MODULE = 'config.settings'\n\
DJANGO_ENV_SERVER_ADDR     = '127.0.0.1'\n\
DJANGO_ENV_SERVER_PORT     = '8000'\n" % os.path.dirname(__file__))

    else:
        locals()[sys.argv[1]](sys.argv[2])