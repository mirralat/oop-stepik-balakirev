class Book:
    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        dct = {'title': str, 'author': str, 'pages': int, 'year': int}
        if dct[key] != type(value):
            raise TypeError("Неверный тип присваиваемых данных.")
        super().__setattr__(key, value)


book = Book(title='Python ООП', author='Сергей Балакирев', pages=123, year=2022)