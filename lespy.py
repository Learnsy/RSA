from random import *


def hl():  # Вызов справки
    print('Введите "Зашифровать" для шифра текста')
    print('Введите "Расшифровать" для расшифровки текста')
    print('Введите "Завершить" для завершения работы')


def generate_prime_number(p: int) -> int:  # Создание простого числа
    i = 1
    while i < p:
        if p % i > 0:
            i += 1
        else:
            p += 1
            i = 1
    return p


def ran(f):  # Выдача случайного числа
    if f == 'p':
        i = 1000
    else:
        i = 0
    p = randint(2000 + i, 3000 + i)
    j = generate_prime_number(p)
    return j


def nn():
    p = ran('p')
    q = ran('q')


def shn():
    m = int(input('Введите текст:  '))


r = True
while r == True:
    word = input('Введите команду:   ')
    if word == 'Завершить':
        r = False
    elif word == 'Зашифровать':
        shn()
    elif word == 'Помощь':
        hl()
    else:
        print('Команда неопознана')
        hl()
