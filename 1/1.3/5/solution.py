class Dictionary:
    rus = 'Питон'
    eng = 'Python'

try:
    x = getattr(Dictionary, 'rus_word')
    print(x)
except AttributeError:
    x = getattr(Dictionary, 'rus_word', False)
    print(x)