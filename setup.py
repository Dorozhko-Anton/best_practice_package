from __future__ import print_function
from setuptools import setup, find_packages
import sys

import project


setup(
    name='project',
    version=project.__version__,
    url='',
    license='',
    author='',
    tests_require=['pytest'],
    install_requires=[],
    cmdclass={'test': PyTest},
    author_email='',
    description='',
    long_description=long_description,
    packages=['project'],
    include_package_data=True,
    platforms='any',
    test_suite='',
    classifiers = [
        'Programming Language :: Python',
        ],
    extras_require={
    },
    scripts = [''],
    
)