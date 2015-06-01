import os, sys
from distutils.core import setup

try:
    with open('README', 'rt') as readme:
        description = '\n' + readme.read()
except IOError:
    # maybe running setup.py from some other dir
    description = ''

setup(
    # metadata
    name='macholib',
    description='Library for analyzing MachO files',
    long_description=description,
    license='Public domain',
    version='1.8',
    author='Eli Bendersky',
    maintainer='Eli Bendersky',
    author_email='eliben@gmail.com',
    url='https://github.com/eliben/pyelftools',
    platforms='Cross Platform',
    classifiers = [
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        ],

    # All packages and sub-packages must be listed here
    packages=[
        'macholib',
        'macholib.MachO',
        'macholib.SymbolTable',
        'macholib.mach_o',
        ],

    scripts=[]
)
