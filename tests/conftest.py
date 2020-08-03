"""
PyTest Fixtures.
"""

# noinspection PyPackageRequirements
import pytest
from cement import fs


# noinspection PyUnusedLocal
@pytest.fixture(scope="function")
def tmp(request):
    """
    Create a `tmp` object that generates a unique temporary directory, and file
    for each test function that requires it.
    """
    t = fs.Tmp()
    yield t
    t.remove()
