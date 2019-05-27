#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

with open('README.md', 'r', encoding='utf-8') as fd:
    readme = fd.read()

with open('requirements.txt', encoding='utf-8') as fd:
    requirements = fd.read()

setup(
    name='loadtest',
    version='0.0.1',
    description="Load testing tool",
    long_description=readme,
    long_description_content_type='text/markdown',
    author="George Watson",
    author_email='geowatson@nullteam.info',
    packages=find_packages(),
    install_requires=requirements,
    keywords='loadtest'
)
