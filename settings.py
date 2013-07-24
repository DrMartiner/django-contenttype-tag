# -*- coding: utf-8 -*-

import sys
import os.path

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ''))
sys.path.insert(0, ROOT)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

SECRET_KEY = '!!!very_secret!!!'
ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'generic_ct_tag',
)