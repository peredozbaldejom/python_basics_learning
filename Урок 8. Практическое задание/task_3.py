"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class ListChecking(Exception):
    def __init__(self, txt):
        self.txt = txt


data = input().split()

for i in data:
    print(type(i))
    try:
        if type(i) != 'list':
            raise ListChecking(f'{i} this is not a number')
    except ListChecking as err:
        print(err)

    else:
        print('all items are numbers')
