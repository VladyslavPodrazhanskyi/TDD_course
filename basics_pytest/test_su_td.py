def setup_module():          # module as arg
    print("Setup Module!")


def teardown_module():         # module as arg
    print("Teardown Module!")


def setup_function(function):
    if function == test1:
        print("setup test1")
    elif function == test2:
        print("setup test2")
    else:
        print("setup unknown test")


def teardown_function(function):
    if function == test1:
        print("teardown test1")
    elif function == test2:
        print("teardown test2")
    else:
        print("teardown unknown test")



def test1():
    print("executing test1")
    assert True


def test2():
    print("executing test2")
    assert True


def test3():
    print("executing test3")
    assert True