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
    python_requires='~=3.7',
    install_requires=[
        'dnspython',
        'marshmallow',
        'marshmallow_dataclass',
        'python-dateutil',
        'cement~=3.0',
        'jinja2',
        'pyyaml',
        'colorlog',
        'semver',
        'jwt',
        'iso8601',
        'tabulate',
        'pyOpenSSL',
        'requests',
        'aenum',
        'colorama',
        'cryptography'
    ],
    extras_require={
        'aws': ['boto3', 'ec2_metadata'],
        'azure_cloud': ['azure-identity', 'azure-mgmt-resource', 'azure-mgmt-compute', 'azure-mgmt-network'],
        'gcp': ['google-api-python-client'],
        'oracle_cloud': ['oci'],
        'okta': ['okta'],
        'azure_ad': ['azure-identity', 'msgraph-core']
    },
    entry_points={'console_scripts': [
        "banyan=banyan.main:main"
    ]},
)
