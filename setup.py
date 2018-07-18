#!/usr/bin/env python

from distutils.core import setup

setup(name='helpdful',
      version='0.1',
      description='pdf generating thing!',
      author='Kent Daleng',
      author_email='kent.stefan.daleng@nav.no',
      packages=['helpdful'],
      install_requires=['reportlab', 'lxml', 'svglib==0.9.0', 'bs4', 'flask'],
      # PS: pip will complain about svglib being the wrong version, but we have to claim
      # there's been a version bump, otherwise an old version will get pulled from pypi
      dependency_links=["git+https://github.com/deeplook/svglib#egg=svglib-0.9.0"]
)
