
from cement.utils.version import get_version as cement_get_version

VERSION = (0, 29, 1, 'final', 1)


def get_version(version=VERSION):
    return cement_get_version(version)
