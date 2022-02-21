'''
File: setup.py
Project: PyEnzyme
Author: Jan Range
License: BSD-2 clause
-----
Last Modified: Wednesday June 23rd 2021 9:57:56 pm
Modified By: Jan Range (<jan.range@simtech.uni-stuttgart.de>)
-----
Copyright (c) 2021 Institute of Biochemistry and Technical Biochemistry Stuttgart
'''

import setuptools
from setuptools import setup

setup(
    name='PyEnzyme',
    version='1.2.1',
    description='Handling of EnzymeML files',
    url='https://github.com/EnzymeML/PyEnzyme',
    author='Range, Jan',
    author_email='jan.range@simtech.uni-stuttgart.de',
    license='BSD2 Clause',
    packages=setuptools.find_packages(),
    install_requires=[
        'python-libsbml',
        'numpy',
        'pandas',
        'python-libcombine',
        'scipy',
        'texttable',
        'pydataverse',
        'pydantic',
        'deprecation',
        'deepdiff',
        'python-multipart',
        'fastapi',
        'uvicorn',
        'easyDataverse',
        'pyDaRUS',
        'openpyxl',
        'numexpr',
        'seaborn',
        'plotly'
    ],
    extras_require={
        'test': [
            'pytest-cov'
        ],
        'examples': [
            'xmltodict'
        ]
    },
)
