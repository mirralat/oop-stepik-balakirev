class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        ret = [f'{i.name}-{i.price}' for i in self.goods]
        return ret


cart = Cart()
cart.add(TV('Lenovo', 1))
cart.add(TV('Lenovo', 1))
cart.add(Table('Ikea', 2))
cart.add(Notebook('Notepad++', 2))
cart.add(Notebook('Notepad++', 2))
cart.add(Cup('Blue', 1000))
