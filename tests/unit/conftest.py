import pytest

@pytest.fixture(scope="session")
def dummy_fixture():
    return 10

