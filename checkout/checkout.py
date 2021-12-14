class AddWithoutPriceException(Exception):
    pass

class Discount:
    def __init__(self, min_disc_num, price):
        self.min_disc_num = min_disc_num
        self.price = price


class Checkout:
    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def add_item_price(self, item, price):
        self.prices[item] = price

    def add_item(self, item):
        if item not in self.prices:
            raise AddWithoutPriceException
        self.items[item] = self.items.get(item, 0) + 1

    def add_discount_rule(self, item, min_disc_num, price):
        discount = Discount(min_disc_num, price)
        self.discounts[item] = discount

    def calculate_total(self):
        total = 0
        for item, num in self.items.items():
            total += self.calculate_total_item(item, num)
        return total

    def calculate_total_item(self, item, num):
        total_item = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if num >= discount.min_disc_num:
                dif_price = self.prices[item] - discount.price
                total_item_discount = dif_price * (num + 1 - discount.min_disc_num)
            else:
                total_item_discount = 0
            total_item += self.prices[item] * num - total_item_discount
        else:
            total_item += self.prices[item] * num
        return total_item






