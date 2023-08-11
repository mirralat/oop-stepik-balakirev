import re
import random
import string


class EmailValidator:

    def __new__(cls, *args, **kwargs):  # запрет создания экземпляра
        return None

    @classmethod
    def get_random_email(cls):
        random_st = ''
        pattern = string.ascii_lowercase + string.ascii_uppercase + string.digits + '_'
        strlen = random.randint(1, 50)
        for i in range(strlen):
            random_st += random.choice(pattern)
        return f'{random_st}@gmail.com'

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        if len(email) > 100:
            return False
        if not re.match('^\w{0,}@{1}\w{0,}\.\w{0,}$', email):
            return False
        position = 0
        for i in email:
            if i != '@':
                position += 1
            else:
                break
        if position > 50:
            return False
        return True

    @staticmethod
    def __is_email_str(email):
        if type(email) == str:
            return True
        return False

