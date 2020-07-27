
from setuptools import setup, find_packages
from banyan.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='pybanyan',
    version=VERSION,
    description='API library and command-line interface for Banyan Security',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Todd Radel',
    author_email='todd@banyansecurity.io',
    url='https://github.com/banyansecurity/pybanyan/',
    license='apache',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'banyan': ['templates/*']},
    include_package_data=True,
    entry_points={'console_scripts': [
        "banyan = banyan.main:main"
    ]},
)
