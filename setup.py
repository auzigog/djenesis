#!/usr/bin/env python

from distutils.core import setup

setup(name='djenesis',
    version='0.9.1',
    description='Bootstrap django projects using a standard project template',
    author='Concentric Sky',
    author_email='django@concentricsky.com',
    url='http://code.google.com/p/djenesis',
    scripts=['djenesis/djenesis.py'],
    packages=['djenesis'],
    package_dir={'djenesis': 'djenesis'},
    package_data={'djenesis': ['project_template']},
)
