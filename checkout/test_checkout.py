"""
- can create instance of Checkout class
- can add item price
- can add item
- can calculate the current total
- can add multiple items and get correct total
- can add discount rules
- can apply discount rules to the total
- exception is thronw for item added without a price
"""

import pytest
from checkout import Checkout
from checkout import AddWithoutPriceException


# def test_assert_true():
#     assert True


# def test_can_instanciate_Checkout():
#     co = Checkout()

@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.add_item_price("a", 1)
    checkout.add_item_price("b", 2)
    return checkout


# def test_can_add_item_price(checkout):
#     checkout.add_item_price("a", 1)
#
#
# def test_can_add_item(checkout):
#     checkout.add_item("a")


def test_calculate_total(checkout):
    checkout.add_item_price("a", 1)
    checkout.add_item("a")
    assert checkout.calculate_total() == 1


def test_multiple_items(checkout):
    checkout.add_item("a")
    checkout.add_item("b")
    assert checkout.calculate_total() == 3


# @pytest.mark.skip
def test_add_discount_rule(checkout):
    checkout.add_item("b")
    checkout.add_item("b")
    checkout.add_item("b")
    checkout.add_item("b")
    checkout.add_discount_rule("b", 3, 1.5)
    assert checkout.calculate_total() == 7


def test_raise_exception(checkout):
    with pytest.raises(AddWithoutPriceException):
        checkout.add_item("c")
