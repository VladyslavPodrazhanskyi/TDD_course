from pytest import approx, raises
import math

def test_int():
    assert 1 == 1


def test_str():
    assert "str" == "str"


def test_float1():
    assert 1.0 == 1.0


def test_float2():
    assert 1.2 + 2.1 == 3.3


def test_float3():
    assert 0.1 + 0.2 == approx(0.3)


def test_list():
    assert list(range(1, 4)) == [1, 2, 3]


def test_dict():
    assert {"1": 1} ==  {"1": 1}


def func_raises_ValueError():
    raise ValueError


def test_ValueError():
    with raises(ValueError):
        func_raises_ValueError()


def test_sqrt():
    assert math.sqrt(4) == 2
    with raises(ValueError):
        math.sqrt(-4)