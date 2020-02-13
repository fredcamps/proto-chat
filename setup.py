#!/usr/bin/env python

# -*- coding: utf-8 -*-

import os.path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


exec(open('proto_chat/version.py').read())

tests_require = [
    'coverage',
    'flake8',
    'pydocstyle',
    'pylint',
    'pytest-pycodestyle',
    'pytest-cov',
    'pytest'
]

version = '0.1.0'

setup(name='proto chat',
      version=__version__,
      description='Just a dummy chat',
      long_description=read('README.rst'),
      author='Fred Campos',
      author_email='fred.tecnologia@gmail.com',
      url='https://github.com/fredcamps/proto-chat',
      classifiers=[
          'Development Status :: 2 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Natural Language :: English',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.8',
      ],
      include_package_data=True,
      packages=['proto_chat'],
      test_suite='tests',
      setup_requires=['pytest-runner'],
      tests_require=tests_require)
