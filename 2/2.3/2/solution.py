class ValidateString:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):
        if type(string) is str:
            if self.min_length <= len(string) <= self.max_length:
                return True
        return False


class StringValue:
    def __init__(self, validator):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.validator.validate(value):
            instance.__dict__[self.name] = value


class RegisterForm:
    login = StringValue(validator=ValidateString(3, 100))
    password = StringValue(validator=ValidateString(3, 100))
    email = StringValue(validator=ValidateString(3, 100))

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        print(f'<form>\n'
                f'Логин: {self.login}\n'
                f'Пароль: {self.password}\n'
                f'Email: {self.email}\n'
                '</form>')
