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


def text(text_str: str) -> list:
    i = len(text_str)
    text_int = []
    j = 0
    for symbol in text_str:
        text_int.append(ord(symbol))
    return text_int


def randint_to_prime(p: int) -> int:  # Создание простого числа
    i = 2
    while i < p:
        if p % i > 0:
            i += 1
        else:
            p += 1
            i = 2
    print(str(p))
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


def key() -> tuple:  # Генератор ключей
    e = randint(10, 99)
    n, fun = nn()
    i = 2
    while i <= e:
        if fun % i == 0 and e % i == 0:
            i = 2
            e += 1
        else:
            i += 1
    d = randint(100, 999)
    while d * e % fun != 1:
        d += 1
    public_key: PublicKey = PublicKey(e=e, n=n)
    private_key: PrivateKey = PrivateKey(d=d, n=n)
    return public_key, private_key


def encrypt_text_to_bytes(encrypt_text: list) -> bytes:
    return b''.join(item.to_bytes(4, "big") for item in encrypt_text)


def encrypt():
    text_str = input('Введите текст:  ')
    text_int = text(text_str)
    encrypt_text = []
    public_key, private_key = key()
    for j in range(len(text_int)):
        encrypt_text.append(text_int[j] ** private_key.d % private_key.n)
    with open('encrypt_text.txt', 'wb') as file:
        to_file_bytes = encrypt_text_to_bytes(encrypt_text)
        file.write(to_file_bytes)
    print('Ключ для расшифровки: ' + str(public_key.e) + ', '+ str(public_key.n))


is_working = True

while is_working:
    word = input('Введите команду:   ')
    if word == 'Завершить':
        is_working = False
    elif word == 'Получить ключ':
        public_key, private_key = key()
        print('Открытый ключ:' + str(public_key.e) + ', ' + str(public_key.n))
    elif word == 'Зашифровать':
        encrypt()
    elif word == 'Помощь':
        show_help_message()
    else:
        print('Команда неопознана')
        show_help_message()
