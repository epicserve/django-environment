#!/usr/bin/python
import os
project_name = os.path.basename(os.getenv("VIRTUAL_ENV"))

try:
	from django.conf import settings
except ImportError:
	try:
		exec "from %s.config import settings" % project_name
	except ImportError:
		exec "from %s import settings" % project_name

def get_var(var_name, default=''):
	val = getattr(settings, var_name, default)
	print val
	
def get_path(var_name):
	val = get_var(var_name, [])
	val = ":".join(val)
	print val
	
if __name__ == '__main__':
	import sys
	
	locals()[sys.argv[1]](sys.argv[2])