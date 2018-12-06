#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup module for the duallog package

This module configures setuptools so that it can create a distribution for the
duallog package.
"""

# Import required system libraries.
import io
from os import path
import setuptools

# Load the readme.
maindir = path.abspath(path.dirname(__file__))
with io.open(path.join(maindir, 'README.md'), encoding='utf-8') as file:
    readme = file.read()

# Configure setuptools.
setuptools.setup(name='duallog',
                 version='0.12',
                 description='Parallel logging to console and logfile',
                 long_description=readme,
                 long_description_content_type='text/markdown',
                 license='MIT',
                 url='https://github.com/acschaefer/duallog',
                 author='Alexander Schaefer',
                 author_email='acschaefer@users.noreply.github.com',
                 maintainer='Alexander Schaefer',
                 include_package_data=False,
                 packages=['duallog'],
                 classifiers=[
                     'License :: OSI Approved :: MIT License',
                     'Programming Language :: Python :: 2',
                     'Programming Language :: Python :: 2.6',
                     'Programming Language :: Python :: 2.7',
                     'Programming Language :: Python :: 3',
                     'Programming Language :: Python :: 3.3',
                     'Programming Language :: Python :: 3.4',
                     'Programming Language :: Python :: 3.5',
                     'Programming Language :: Python :: 3.6',
                     'Programming Language :: Python :: 3.7',
                     'Operating System :: OS Independent'])
