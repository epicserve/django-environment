#!/usr/bin/env python


import sys, os, re


def main():
    os.system('rm "$WORKON_HOME/django_env"')
    f = open('%s/postmkvirtualenv' % os.environ.get('WORKON_HOME'), 'r')
    fcontents = f.read()
    f.close()
    f = open('%s/postmkvirtualenv' % os.environ.get('WORKON_HOME'), 'w')
    replacement_text = re.sub(r'\s+source \$WORKON_HOME/django_env/bin/postmkvirtualenv\s+', '', fcontents)
    f.write(replacement_text)
    f.close()
    print "Django-environment uninstalled."


if __name__ == '__main__':
    main()