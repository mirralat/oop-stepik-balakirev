class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if ((type(self.a) not in (int, float)) or self.a <= 0) or ((type(self.b) not in (int, float)) or self.b <= 0) or ((type(self.c) not in (int, float)) or self.c <=0):
            return 1
        if self.a >= self.b + self.c or self.b >= self.a + self.c or self.c >= self.a+self.b:
            return 2
        return 3


a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
tr.is_triangle()
