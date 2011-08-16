# Django-environment

A plugin for virtualenvwrapper that makes setting up and creating new Django environments easier.

## Quick Install Instructions

Pip install django-environment

    $ pip install django-environment
    $ python -c "from django_env.bin import install; install.main();"

Optionally you can make the `--no-site-packages` argument the default argument when making a new virtual environment. Edit your `~/.profile` or `~/.bashrc` to add the following alias.

    alias mkvirtualenv="mkvirtualenv --no-site-packages"

## Optional Config Settings

You can add optional settings that can change the default install behavior. One of the best settings is `DJANGO_BASE_SITE_URL`, if you have a Django base site on your local file system, Github, Bitbucket or any GIT, HG or SVN repository, you can have Django-environment setup a new environment using your own custom base site!

To setup and use the optional config settings, all you need to do is add the file `~/.django_env_config` with any of the following settings. Alternatively, if you would prefer to put your config file somewhere else, then all you need to do is something like, `export DJANGO_ENV_CONFIG_PATH=/Users/username/.dotfiles/django_env_config` in your `~/.profile` or `~/.bashrc` (depending on your OS).

    # Controls whether or not to prompt the user during the setup of a new environment. Use N for No or Y for Yes.
    USE_DEFAULTS="N"

    # Controls whether or not to create a basic default fabfile template.
    CREATE_FABFILE="Y"

    # Sets the URL to use when pip installs Django. If blank Django will be
    # installed using, "pip install django". If you want to save download time
    # you could use something like, "/usr/local/src/django/Django-1.3.tar.gz"
    # to use a local tar gzipped version.
    DJANGO_SRC_URL=""

    # Use this setting to set the url of a Django base site. Currently Django-
    # environment has been tested with Github, Bitbucket and a privately hosted
    # SVN repository.
    #
    # Example URLs:
    # git+git://github.com/epicserve/django-base-site.git
    # hg+https://epicserve@bitbucket.org/epicserve/django-base-site
    # svn+ssh://user@ssh.yourdomain.com/path/to/django-base-site/trunk
    # file:///Users/username/code/django/django-base-site
    DJANGO_BASE_SITE_URL=""

    # Use this setting to change the default Django CONFIG_PATH.
    CONFIG_PATH="config"

    # Change the default Django development server address.
    SERVER_ADDR="127.0.0.1"

    # Change the default Django development server port.
    SERVER_PORT="8000"

    # If you Django base site has requirement files you can have
    # Django-environment install your pip requirements after your new
    # environment is installed.
    # Example: POST_PIP_CMD="install -r config/requirements.txt -r config/dev-requirements.txt"
    POST_PIP_CMD=""


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
