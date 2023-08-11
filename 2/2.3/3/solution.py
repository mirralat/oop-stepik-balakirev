class StringValue:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, value):
        if type(value) is str:
            if self.min_length <= len(value) <= self.max_length:
                return True

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.validate(value) is True:
            instance.__dict__[self.name] = value


class PriceValue:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def validate(self, value):
        if type(value) in (float, int):
            if self.min_value <= int(value) <= self.max_value:
                return True

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.validate(value) is True:
            instance.__dict__[self.name] = value


class Product:
    name = StringValue(2, 50)
    price = PriceValue(0, 10000)

    def __init__(self, name, price):
        self.name = name
        self.price = price


class SuperShop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)

