# -*- coding: utf-8 -*-

import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-contenttype-tag',
    version='1.0',
    packages=['generic_ct_tag'],
    include_package_data=True,
    license='MIT',
    description='Easy application for get content type at template',
    long_description=README,
    url='http://github.com/drmartiner/django-contenttype-tag/',
    author='DrMartiner',
    author_email='DrMartiner@GMail.Com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django>=1.3',
    ],
)