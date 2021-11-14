from random import *


def show_help_message():  # Вызов справки
    print('Введите "Зашифровать" для шифра текста')
    print('Введите "Расшифровать" для расшифровки текста')
    print('Введите "Завершить" для завершения работы')


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


def encrypt():
    m = int(input('Введите текст:  '))


is_working = True

while is_working:
    word = input('Введите команду:   ')
    if word == 'Завершить':
        is_working = False
    elif word == 'Зашифровать':
        encrypt()
    elif word == 'Помощь':
        show_help_message()
    else:
        print('Команда неопознана')
        show_help_message()
