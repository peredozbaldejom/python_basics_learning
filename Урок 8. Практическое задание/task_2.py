"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ZeroEx(Exception):
    def __init__(self, txt):
        self.txt = txt


def div(x, y):
    try:
        if y == 0:
            raise ZeroEx('error')
    except ZeroEx as er:
        print(er)

    else:
        print(x / y)


div(100, 0)
