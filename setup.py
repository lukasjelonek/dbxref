from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dbxref',
    version='0.1.0',
    description='A library for resolving database cross references',
    long_description=long_description, 
    url='https://git.computational.bio.uni-giessen.de/SOaAS/dbxref',
    author='Lukas Jelonek',
    author_email='Lukas.Jelonek@computational.bio.uni-giessen.de',
    keywords='dbxref',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    package_data={'dbxref':['*.yaml']},
    install_requires=[
      'requests',
      'cachecontrol',
      'pyyaml',
      'lockfile'
    ],
    entry_points={ 
        'console_scripts': [
          'dbxref=dbxref.main:main',
        ],
    },
)
