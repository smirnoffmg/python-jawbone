#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'requests',
]

test_requirements = [
    'mock',
]

setup(
    name='python_jawbone',
    version='0.1.1',
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    long_description=readme + '\n\n' + history,
    author="Maxim Smirnoff",
    author_email='smirnoffmg@gmail.com',
    url='https://github.com/budurli/python-jawbone',
    packages=[
        'python_jawbone',
    ],
    package_dir={'python_jawbone':
                 'python_jawbone'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='python_jawbone',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
