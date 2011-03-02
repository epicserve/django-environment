# Django-environment

A plugin for virtualenvwrapper that makes setting up and creating new Django environments easier.

## Quick Install Instructions

Pip install django-environment

    $ pip install git+http://github.com/epicserve/django-environment.git@0.3.X#egg=django-environment
    $ python -c "from django_env.bin import install; install.main();"

Optionally you can make the `--no-site-packages` argument the default argument when making a new virtual environment. Edit your `~/.profile` or `~/.bashrc` to add the following alias.

    alias mkvirtualenv="mkvirtualenv --no-site-packages"

## Create a new Django Environment for a Project

1. Create your container directory for your project. For example if you're working on the website example.com you might want to create a container directory called "example.com" in your home `~/Sites` directory.

        $ cd ~/Sites
        $ mkdir example.com
        $ cd example.com

2. Next you create your virtual environment and add your initial Django configuration files inside your Django project container directory or inside the Django project root directory.

Run the `mkvirtualenv` command followed by the name you want to give your virtual environment. This is usually just an abbreviation of your website or your website domain name without the [TLD](http://en.wikipedia.org/wiki/Top-level_domain) extension.

    $ mkvirtualenv --no-site-packages example

The previous command should give you an output like the following. Just answer all the prompts and when it finishes you should have a newly setup Django environment. Pay close attention to the question about the path to your config directory. The default setting should work well for most people.

    New python executable in example/bin/python
    Installing setuptools............done.
    virtualenvwrapper.user_scripts Creating /Users/username/.virtualenvs/example/bin/predeactivate
    virtualenvwrapper.user_scripts Creating /Users/username/.virtualenvs/example/bin/postdeactivate
    virtualenvwrapper.user_scripts Creating /Users/username/.virtualenvs/example/bin/preactivate
    virtualenvwrapper.user_scripts Creating /Users/username/.virtualenvs/example/bin/postactivate
    Is this a Django-enviroment your creating (y/n)? [Default: y] 
    Enter the python path to the config directory (i.e. Where your settings.py, manage.py and urls will go). Use just . if you want the config files in your current project root. [Default: example.config] 
    Development server address? [Default: 127.0.0.1] 
    Development server address? [Default: 8000] 
    Create a blank Fabric fabfile in your project (y/n)? [Default: y] 
    Unpacking /Users/username/Downloads/Django-1.2.3.tar.gz
      Running setup.py egg_info for package from file:///Users/username/Downloads/Django-1.2.3.tar.gz
        warning: no files found matching 'django/dispatch/LICENSE.txt'
        warning: no files found matching '*' under directory 'examples'
    Installing collected packages: Django
      Running setup.py install for Django
        changing mode of build/scripts-2.6/django-admin.py from 644 to 755
        warning: no files found matching 'django/dispatch/LICENSE.txt'
        warning: no files found matching '*' under directory 'examples'
        changing mode of /Users/username/.virtualenvs/example/bin/django-admin.py to 755
    Successfully installed Django
    Cleaning up...

    Your Django-environment "example" has been activated.

    Django-environment Commands:
    runserver      Starts the Django development server 
    deactivate     Deactivates the current Django-environment 
    workon <name>  Work on a different Django-environment

    (example)oconnor@shiny:~/Sites/django_env_test/example.com$

Start the development server for your new project.

	$ runserver

The previous command should give you an output like the following. Now if you go to the URL it gives you in your browser you should get the Django "It worked!" page. Now you're readying to start working on your new Django website.

    0 errors found

    Django version 1.2.3, using settings 'example.config.settings'
    Development server is running at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
