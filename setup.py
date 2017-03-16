#!/usr/bin/env python

from setuptools import setup

setup(
    # GETTING-STARTED: set your app name:
    name='CruzRojaTijuana',
    # GETTING-STARTED: set your app version:
    version='1.0',
    # GETTING-STARTED: set your app description:
    description='Website',
    # GETTING-STARTED: set author name (your name):
    author='Mint IT Media',
    # GETTING-STARTED: set author email (your email):
    author_email='info@mintitmedia.com',
    # GETTING-STARTED: set author url (your url):
    url='http://www.python.org/sigs/distutils-sig/',
    # GETTING-STARTED: define required django version:
    install_requires=[
        'appdirs==1.4.3',
        'bleach==2.0.0',
        'Django==1.4.6',
        'django-tinymce==2.0.5',
        'filebrowser-safe==0.4.7',
        'future==0.16.0',
        'grappelli-safe==0.4.6',
        'html5lib==0.95',
        'Mezzanine==1.4.10',
        'oauthlib==2.0.1',
        'olefile==0.44',
        'packaging==16.8',
        'Pillow==4.0.0',
        'pyparsing==2.2.0',
        'python-slugify==1.1.4',
        'pytz==2016.10',
        'requests==1.2.3',
        'requests-oauthlib==0.3.2',
        'six==1.10.0',
        'South==1.0.2',
        'twitter==1.17.1',
        'Unidecode==0.4.18'
    ],
    dependency_links=[
        'https://pypi.python.org/simple/django/'
    ],
)
