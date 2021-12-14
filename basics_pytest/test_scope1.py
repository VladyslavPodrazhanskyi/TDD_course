import pytest


@pytest.fixture(scope='session', autouse=True)
def setup_session():
    print("\nSetup session")


@pytest.fixture(scope="module", autouse=True)
def setup_module1():
    print("\nSetup module 1")


@pytest.fixture(scope='function', autouse=True)
def setup_module():
    print("\nSetup function")


def test1():
    print("Executing test1")
    assert True


def test2():
    print("Executing test2")
    assert True
