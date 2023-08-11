class Shop:
    def __init__(self, name):
        self.goods = []
        self.name = name

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    __id__instance = 1

    def __init__(self, name, weight, price):
        self.id = Product.__id__instance
        Product.__id__instance += 1
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        dct_iterable = {'weight': (int, float), 'price': (int, float)}
        dct_non_iterable = {'id': int, 'name': str}
        if type(value) in (int, float) and value < 0:
            raise TypeError("Неверный тип присваиваемых данных.")
        if key in dct_iterable.keys():
            if type(value) not in dct_iterable[key]:
                raise TypeError("Неверный тип присваиваемых данных.")

        elif key in dct_non_iterable.keys():
            if dct_non_iterable[key] != type(value):
                raise TypeError("Неверный тип присваиваемых данных.")

        super().__setattr__(key, value)

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")
