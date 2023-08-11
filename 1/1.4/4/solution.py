import sys

class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def select(self, a, b):
        return self.lst_data[a:b+1]

    def insert(self, data):
        pattern = {}
        for i in range(len(data)):
            pattern[self.FIELDS[i]] = data[i]
        self.lst_data.append(pattern)

db = DataBase()
lst_in = list(map(str.strip, sys.stdin.readlines()))