#!/usr/bin/env python
import os
import importlib

try:
    import sys
    importlib.reload(sys).setdefaultencoding("UTF-8")
except:
    pass

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

long_description = read('README.rst')

__doc__ = long_description

setup(
    name='energistream',
    version='0.3',
    description='EnergiStream is a client for the EnergiStream API, an energy information and demand management platform by MelRok, LLC.',
    long_description=read('README.rst'),
    author='MelRok -- Modeling and Analytics',
    url='https://github.com/Melrok/energistream',
    packages=['energistream'], #find_packages()
    requires=['pandas','requests']
)
