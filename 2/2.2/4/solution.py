class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        self.x = x
        self.y = y

    @classmethod
    def validator(cls, value):
        if type(value) in (int, float):
            if cls.MIN_COORD <= value <= cls.MAX_COORD:
                return True
        return False

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if self.validator(value) is True:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if self.validator(value) is True:
            self.__y = value

    @staticmethod
    def norm2(vector):
        return vector.x * vector.x + vector.y * vector.y


v1 = RadiusVector2D()        # радиус-вектор с координатами (0; 0)
v2 = RadiusVector2D(1)       # радиус-вектор с координатами (1; 0)
v3 = RadiusVector2D(1025, 2)
print(v1.norm2(v3))
