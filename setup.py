#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import sys
import codecs
from setuptools import setup, find_packages
from manhuagui import __version__, __author__, __email__

with open('requirements.txt') as f:
    requirements = [l for l in f.read().splitlines() if l]


setup(
    name='manhuagui',
    version=manhuagui.__version__,
    description='manhuagui.com comics downloader',
    keywords=['manhuagui', 'comics'],
    author='KellyHwong',
    author_email='dianhuangkan@gmail.com',
    maintainer='KellyHwong',
    maintainer_email='dianhuangkan@gmail.com',
    license='Apache',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/7sDream/zhihu-oauth',
    install_requires=requirements,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)