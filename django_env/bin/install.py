#!/usr/bin/env python


import sys, os


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
    command = "echo '\n\nsource $WORKON_HOME/django_env/bin/postmkvirtualenv\n' >> \"$WORKON_HOME/postmkvirtualenv\""
    os.system(command)
    
    print """

Django-environment is now installed. To create a django-environment run
the following.

mkvirtualenv [project_name]

Example:
mkvirtualenv example

"""


if __name__ == '__main__':
    main()
