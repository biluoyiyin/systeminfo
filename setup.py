#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: Put package requirements here
]

setup_requirements = [
    # TODO(biluoyiyin): Put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    # TODO: Put package test requirements here
]

setup(
    name='systeminfo',
    version='0.1',
    description="It is SE assignment2",
    long_description=readme + '\n\n' + history,
    author="Xuanchen Yao",
    author_email='xuanchen.yao@ucdconnect.ie',
    url='https://github.com/biluoyiyin/systeminfo',
    packages=find_packages(include=['systeminfo','sysinfo']),
    entry_points={
        'console_scripts': [
            'comp30670_systeminfo=systeminfo.main:main',
        ],
    },
    include_package_data=True,
    install_requires=requirements,
    license="GPL3",
    zip_safe=False,
    keywords='systeminfo',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
