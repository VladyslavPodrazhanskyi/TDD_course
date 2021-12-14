import pytest


class TestClass:

    @classmethod
    def setup_class(cls):
        print("Setup for TestClass")

    @classmethod
    def teardown_class(cls):
        print("Teardown for TestClass")

    def setup_method(self, method):
        if method == self.test1:
            print("Setup method test1")
        elif method == self.test2:
            print("Setup method test2")
        else:
            print("Setup unknown test method")

    def teardown_method(self, method):
        if method == self.test1:
            print("Teardown method test1")
        elif method == self.test2:
            print("Teardown method test2")
        else:
            print("Teardown unknown test method")

    def test1(self):
        print("test1 executing")
        assert True

    def test2(self):
        print("test2 executing")
        assert True

    def test3(self):
        print("test3 executing")
        assert True


