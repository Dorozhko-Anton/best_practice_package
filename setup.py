from __future__ import print_function
from setuptools import setup, find_packages
import sys

import ossproject

long_description = """
This package is a practical exercice of packaging
"""

setup(
    name='ossproject',
    version=ossproject.__version__,
    url='',
    license='MIT',
    author='Anton Dorozhko',
    tests_require=['pytest'],
    install_requires=['numpy'],
    author_email='dorozhko.a@gmail.com',
    description='packaging package',
    long_description=long_description,
    packages=['project'],
    include_package_data=True,
    platforms='any',
    classifiers = [
        'Programming Language :: Python',
        ],
    extras_require={
        'testing': ['pytest'],
    },
    scripts = [''],

)