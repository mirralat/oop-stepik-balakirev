import re


class CardCheck:
    valid_number = '^\d{4}-\d{4}-\d{4}-\d{4}$'
    valid_name = '^[A-Z]{1,}\s[A-Z]{1,}$'

    @classmethod
    def check_card_number(cls, number):
        if re.match(cls.valid_number, number):
            return True
        return False

    @classmethod
    def check_name(cls, name):
        if re.match(cls.valid_name, name):
            return True
        return False
