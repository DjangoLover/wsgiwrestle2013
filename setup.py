#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = ""
history = ""

setup(
    name='the_game',
    version='0.0.1',
    description="The Game is a simple game engine",
    long_description=readme + '\n\n' + history,
    author='Wayne Werner',
    author_email='waynejwerner@gmail.com',
    url='https://github.com/waynew/wsgi_wrestle2013',
    packages=[
        'the_game',
    ],
    package_dir={'the_game': 'the_game'},
#    entry_points={
#        'console_scripts':[
#            'the_game = the_game.main:start',
#        ],
#    },
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='pipe_dream',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
)
