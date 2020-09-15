# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

__version__ = '1.0.0'
__description__ = 'Api crud de lista de tarefas'
__long_description__ = 'This is an API to Flask Api Users'

__author__ = 'Ana Paula Lopes'
__author_email__ = '@gmail.com'

setup(
    name='api-task-list',
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    packages=find_packages(),
    license='MIT',
    description=__description__,
    long_description=__long_description__,
    url='https://github.com/anaplopes/task-list.git',
    keywords='API, Postgres',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3.8.2',
        'License :: OSI Approved :: MIT License',
    ],
)
