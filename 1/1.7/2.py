from string import ascii_lowercase, digits


# здесь объявляйте классы TextInput и PasswordInput


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


class TextInput:
    def __init__(self, name, size=10):
        self.check_name(name)
        self.name = name
        self.size = size

    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):
        if type(name) != str or len(name) < 3 or len(name) > 50:
            raise ValueError("некорректное поле name")

        if not set(name) < set(cls.CHARS_CORRECT):
            raise ValueError("некорректное поле name")


class PasswordInput:
    def __init__(self, name, size=10):
        self.check_name(name)
        self.name = name
        self.size = size

    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):
        if type(name) != str or len(name) < 3 or len(name) > 50:
            raise ValueError("некорректное поле name")

        if not set(name) < set(cls.CHARS_CORRECT):
            raise ValueError("некорректное поле name")


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()