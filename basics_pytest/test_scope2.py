import pytest


@pytest.fixture(scope="module", autouse=True)
def setup_module2():
    print("\nSetup module 2")


@pytest.fixture(scope="class", autouse=True)
def setup_class2():
    print("\nSetup class 2")


@pytest.fixture(scope="function", autouse=True)
def setup_function2():
    print("\nSetup function 2")


class TestClass2:
    def test_it(self):
        print("Test it")
        assert True

    def test_it2(self):
        print("Test it 2")
        assert True
