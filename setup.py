#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from thumbor_padding_filter import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'colorama',
    'preggy',
    'ipdb',
    'coveralls',
    'numpy',
]

setup(
    name='thumbor_padding',
    version=__version__,
    description='Padding filter for thumbor.',
    long_description='''
Padding filter for thumbor.
''',
    keywords='thumbor filter',
    author='Derek Lucas',
    author_email='derek.lucas@arcivr.com',
    url='https://github.com/arcivr/thumbor-padding',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pillow',
    ],
    extras_require={
        'tests': tests_require,
    }
)
