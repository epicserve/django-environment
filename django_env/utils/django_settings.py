#!/usr/bin/env python

import sys, os

project_name = os.path.basename(os.getenv("VIRTUAL_ENV"))

# try:
# 	exec "from %s.config import settings" % project_name
# except ImportError:
# 	from django.conf import settings

def get_var(var_name, default=''):
	val = getattr(settings, var_name, default)
	print val
	
def get_path(var_name):
	val = get_var(var_name, [])
	val = ":".join(val)
	print val

if __name__ == '__main__':
	
	exec "from %s.config import local_settings as settings" % project_name
	
	locals()[sys.argv[1]](sys.argv[2])