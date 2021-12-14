import pytest


@pytest.fixture()
def setup1():
    print("\nSetup 1")
    yield
    print("\nTeardown 1")


@pytest.fixture()
def setup2(request):
    print("\nSetup 2")

    def teardown_a():
        print("Teardown A")

    def teardown_b():
        print("Teardown B")

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)


def test1(setup1):
    print("Test1 exectuing")
    assert True


def test2(setup2):
    print("Test2 exectuing")
    assert True
