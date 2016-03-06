#!/usr/bin/env python
from setuptools import setup, find_packages

import suckless

setup(name='suckless',
      version=suckless.__versionstr__,
      author='starenka',
      author_email='starenka0@gmail.com',
      url='starenka.net',
      packages=find_packages(),
      include_package_data=True,
      scripts=[],
      install_requires=('django', 'ipdb', 'line_profiler'),
      dependency_links=[],
      setup_requires=('setuptools',),
      tests_require=[],

      zip_safe=False,
      )
