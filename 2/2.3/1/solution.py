class FloatValue:
    @classmethod
    def validate(cls, value):
        if type(value) is not float:
            raise TypeError('Присваивать можно только вещественный тип данных.')

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:
    def __init__(self, N, M):
        self.cells = [[Cell() for _ in range(M)] for _ in range(N)]


table = TableSheet(5, 3)
n = 1.0
for i in range(5):
    for j in range(3):
        table.cells[i][j].value = n
        n += 1.0

for i in range(5):
    print('\n')
    for j in range(3):
        print(table.cells[i][j].value, end=' ')
