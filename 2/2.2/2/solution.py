class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    @classmethod
    def validator(cls, value):
        if type(value) is int and 0 <= value <= 1000:
            return True
        return False

    def show(self):
        print(f'{self.__title}: {self.__width}, {self.__height}')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if self.validator(value) is True:
            self.__width = value
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if self.validator(value) is True:
            self.__height = value
            self.show()
