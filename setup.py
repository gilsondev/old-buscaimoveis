# coding: utf-8

from setuptools import setup

requirements = [
    'flask',
    'import_string',
    'pymongo',
    'tinymongo',
    'tinydb_serialization',
    'dynaconf',
    'awesome_slugify',
    'mistune',
    'flask_simplelogin',
    'flask_admin',
    'flask_wtf',
    'flask_bootstrap',
    'PyYAML',
    'gunicorn'
]


setup(
    name='buscaimoveis',
    version='0.0.1',
    description="Centralize home ads",
    author="Gilson Filho",
    author_email='me@gilsondev.in',
    url='https://github.com/gilsondev/buscaimoveis',
    packages=['buscaimoveis'],
    package_dir={'buscaimoveis': 'buscaimoveis'},
    entry_points={
        'console_scripts': [
            'bimoveis=buscaimoveis.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements
)
