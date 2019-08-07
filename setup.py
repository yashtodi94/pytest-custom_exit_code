#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-custom_exit_code',
    version='0.3.0',
    author='Yash Todi',
    author_email='yashtodi94@gmail.com',
    maintainer='Yash Todi',
    maintainer_email='yashtodi94@gmail.com',
    license='MIT',
    url='https://github.com/yashtodi94/pytest-custom_exit_code',
    description='Exit pytest test session with custom exit code in different scenarios',
    long_description=read('README.rst'),
    py_modules=['pytest_custom_exit_code'],
    python_requires='>2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=['pytest>=4.0.2'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'custom_exit_code = pytest_custom_exit_code',
        ],
    },
)
