#!/usr/bin/env python


import sys
import os


def main():
    django_env_dir = os.path.abspath('%s/../' % os.path.dirname(__file__))
    workon_home = os.environ.get('WORKON_HOME')
    if not workon_home:
        print "ERROR: The $WORKON_HOME environment variable is not set. Please check to make sure you've installed and setup virtualenvwrapper correctly."
        sys.exit()

    # symlink the django_env directory inside the $WORKON_HOME
    command = 'ln -sf %s "$WORKON_HOME/django_env"' % django_env_dir
    os.system(command)

    # add the ejango_env postmkvirtualenv hook to the virtualenvwrapper postmkvirtualenv hook
    postmkvirtualenv_cmd = 'source $WORKON_HOME/django_env/bin/postmkvirtualenv'
    workon_home = os.getenv('WORKON_HOME')
    postmkvirtualenv_path = os.path.join(workon_home, 'postmkvirtualenv')
    fh = open(postmkvirtualenv_path, "r")
    contents = fh.read()
    fh.close()
    if contents.find(postmkvirtualenv_cmd) == -1:
        fh = open(postmkvirtualenv_path, "a")
        fh.write("\n\n%s\n\n" % postmkvirtualenv_cmd)
        fh.close()

    print """

Django-environment is now installed. To create a django-environment run
the following.

mkvirtualenv [project_name]

Example:
mkvirtualenv example

"""


if __name__ == '__main__':
    main()
