from random import *

class PublicKey:
    def __init__(self, e: int, n: int):
        self.e: int = e
        self.n: int = n

class PrivateKey:
    def __init__(self, d: int, n: int):
        self.d: int = d
        self.n: int = n

def show_help_message():  # Вызов справки
    print('Введите "Зашифровать" для шифра текста')
    print('Введите "Расшифровать" для расшифровки текста')
    print('Введите "Завершить" для завершения работы')

def text(text_str: str) -> int:
    i = len(text_str)
    text_int = []
    for j in range(i):
        text_int[j] = ord(text_str[j])
    return text_int

def randint_to_prime(p: int) -> int:  # Создание простого числа
    i = 1
    while i < p:
        if p % i > 0:
            i += 1
        else:
            p += 1
            i = 1
    return p


def generate_prime_number(range_n: str) -> int:  # Выдача случайного числа
    if range_n == 'p':
        i = 1000
    else:
        i = 0
    p = randint(2000 + i, 3000 + i)
    prime: int = randint_to_prime(p)
    return prime


def nn():
    p = generate_prime_number('p')
    q = generate_prime_number('q')
    n = p * q
    fun = (p - 1) * (q - 1)
    return n, fun

def key() -> tuple: # Генератор ключей
    e = randint(100, 999)
    n, fun = nn()
    i = 2
    while i <= e:
        if fun % i == 0 and e % i == 0:
            i = 2
            e += 1
        else:
            i += 1
    d = randint(100, 999)
    while d*e % fun != 1:
        d += 1
    public_key: PublicKey = PublicKey(e=e, n=n)
    private_key: PrivateKey = PrivateKey(d=d, n=n)
    return public_key, private_key

def encrypt():
    text_str = int(input('Введите текст:  '))
    text_int = text(text_str)
    encrypt_text = []
    i = len(text_int)
    for j in range(i):
        encrypt_text[j] = text_int[j] ** PrivateKey.d % PrivateKey.n
    open('encrypt_text.txt', 'w')
    f.write(encrypt_text + '\n')
    print('Ключ для расшифровки: ' + PublicKey.e + PublicKey.n)

is_working = True

while is_working:
    word = input('Введите команду:   ')
    if word == 'Завершить':
        is_working = False
    elif word == 'Получить ключ':
        key()
        print('Открытый ключ:' + str(PublicKey.e) + ',' + str(PublicKey.n))
    elif word == 'Зашифровать':
        encrypt()
    elif word == 'Помощь':
        show_help_message()
    else:
        print('Команда неопознана')
        show_help_message()
