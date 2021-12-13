import pytest


@pytest.fixture()     # autouse=True
def setup():
    print("\nSetup")


def test1(setup):
    print("Test1 executing")
    assert True


@pytest.mark.usefixtures("setup")
def test2():
    print("Test2 executing")
    assert True
