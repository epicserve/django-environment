#!/usr/bin/env python





from distutils.core import setup


setup(
    name='django-environment',
    version=__import__('django_env').__version__,
    description='A plugin for virtualenvwrapper that makes setting up and creating new Django environments easier.',
    long_description=open('README.md').read(),
    author="Brent O'Connor",
    author_email='epicserve@gmail.com',
    url='http://github.com/epicserve/django-environment',
    install_requires=['virtualenvwrapper'],
    packages=['django_env'],
    package_data={
        "django_env": ['bin/*', 'config/*', 'utils/*'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
