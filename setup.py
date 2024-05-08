from setuptools import find_packages, setup, find_namespace_packages

with open('./requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name = 'xlsx2csv',
    version = '0.1.0',
    packages = find_packages(),
    install_requires = requirements,
    entry_points = {
        'console_scripts': [
            'xlsx2csv = xlsx2csv.__main__:main'
        ]
    })
