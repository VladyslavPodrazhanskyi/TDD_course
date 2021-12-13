import pytest


@pytest.fixture(params=[1, 2, 3])  # params - iterable object
def setup(request):
    retval = request.param
    print(f"\nSetup! retval = {retval}")
    return retval


def test1(setup):
    print(f"setup = {setup}")
    print("test1 execting")
    assert True

