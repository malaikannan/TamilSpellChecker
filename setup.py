#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Setup file derived from open-tamil project.
# (C) 2018-2020 Ezhil Language Foundation

from distutils.core import setup
from codecs import open

setup(name='tamilspellchecker',
      version='0.10',
      description='Tamil spell checker',
      author='Malaikannan Sankarasubbu, T. Shrinivasan, Ezhil Language Foundation, et-al',
      author_email='malai128@gmail.com',
      url='https://github.com/Ezhil-Language-Foundation/TamilSpellChecker/',
      install_requires=['open-tamil>=0.96',
                        'bitarray == 1.2.2',
                        'jellyfish == 0.7.2',
                        'mmh3 >= 2.5.1',
                        'requests >= 2.22.0',
                        'urllib3 >= 1.25.6'
                        ],
      packages=['tamilspellchecker'],
      package_dir={'tamilspellchecker': 'tamilspellchecker'},
      package_data={'tamilspellchecker': ['data/*',]},
      license='APACHE',
      scripts=['ProjectMaduraiCrawler.py'],
      platforms='PC,Linux,Mac',
      classifiers=['Natural Language :: Tamil',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4'],
      long_description=open('README.rst','r').read(),
      download_url='https://github.com/Ezhil-Language-Foundation/TamilSpellChecker/archive/v0.10.zip',#pip
      )
