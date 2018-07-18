#!/usr/bin/env python

from distutils.core import setup

setup(name='helpdful',
      version='0.1',
      description='pdf generating thing!',
      author='Kent Daleng',
      author_email='kent.stefan.daleng@nav.no',
      packages=['helpdful'],
      install_requires=['reportlab', 'lxml', 'svglib', 'bs4', 'flask']
)
