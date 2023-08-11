class Car:
    def __init__(self):
        self.__model = None

    @classmethod
    def validator(cls, value):
        if type(value) is str and 2 <= len(value) <= 100:
            return True
        else:
            return False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if self.validator(value) == 1:
            self.__model = value


car = Car()
car.model = 'car'
print(car.model)
