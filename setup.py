from setuptools import setup
import os

# OS X: prevent 'tar' from including resource forks ("._*" files)
os.environ['COPYFILE_DISABLE'] = 'true'

# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
for dirpath, dirnames, filenames in os.walk('django_env', 'virtualenvwrapper'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'):
            del dirnames[i]
    if '__init__.py' in filenames and dirpath != os.path.join('django_env', 'bin'):
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[11:]  # Strip "django_env/" or "django_env\"
        for f in filenames:
            if not f.endswith('.pyc'):  # ignore pyc files
                data_files.append(os.path.join(prefix, f))

packages.append('virtualenvwrapper')
setup(
    name='django-environment',
    version=__import__('django_env').__version__,
    description='A plugin for virtualenvwrapper that makes setting up and creating new Django environments easier.',
    long_description=open('README.md').read(),
    author="Brent O'Connor",
    author_email='epicserve@gmail.com',
    url='http://github.com/epicserve/django-environment',
    install_requires=['virtualenvwrapper'],
    packages=packages,
    package_data={'django_env': data_files},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points={
        'virtualenvwrapper.post_activate': [
            'django_env = virtualenvwrapper.django_env:post_activate',
        ],
        'virtualenvwrapper.post_activate_source': [
            'django_env = virtualenvwrapper.django_env:post_activate_source',
        ],
        'virtualenvwrapper.post_deactivate': [
            'django_env = virtualenvwrapper.django_env:post_deactivate',
        ],
        'virtualenvwrapper.post_deactivate_source': [
            'django_env = virtualenvwrapper.django_env:post_deactivate_source',
        ],
        'virtualenvwrapper.post_mkvirtualenv': [
            'django_env = virtualenvwrapper.django_env:post_mkvirtualenv',
        ],
    },
)
