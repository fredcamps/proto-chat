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
    'pytest-pep8',
    'pytest-cov',
    # for pytest-runner to work, it is important that pytest comes last in
    # this list: https://github.com/pytest-dev/pytest-runner/issues/11
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
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
      ],
      include_package_data=True,
      packages=find_packages(include=['proto_chat*']),
      test_suite='tests',
      setup_requires=['pytest-runner'],
      tests_require=tests_require)
