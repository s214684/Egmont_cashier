"""
Setup for the EGMONT_CASHIER project.
"""

# Imports
# - Python
from setuptools import setup, find_packages
from os import path
from io import open

# Constants
HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()
url='https://github.com/s214684/Egmont_cashier'

# Setup
setup(
    name='egmont_cashier',
    version='0.0.1',
    description='A cashier system for Egmont',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url=url,
    author='s214684',

    classifiers=[
        'Development Status :: 1 - Planning',

        'Programming Language :: Python :: 3.11',
    ],

    keywords='egmont cashier',
    packages=['egmont_cashier', 'egmont_cashier.foodclubs', 'egmont_cashier.person',
              'egmont_cashier.foodclubs.foodclubinfo', 'egmont_cashier.foodclubs.foodclub_participant',
              'egmont_cashier.foodclubs.foodclub', 'egmont_cashier.foodclubs.foodclub_month',
              'egmont_cashier.foodclubs.foodclub_participant'],
    python_requires='>=3.11, <4',
    install_requires=['requests'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    project_urls={
        'Bug Reports': url + '/issues',
        'Source': url,
    },
)

