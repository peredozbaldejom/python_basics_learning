"""
Задание 1.

Реализовать класс «Дата», на уровне класса определить атрибут day_month_year,
присвоить ему значение

В рамках класса реализовать два метода.

Первый, с декоратором @classmethod, должен извлекать число, месяц,
год, преобразовывать их тип к типу «Число» и делать атрибутами класса.

Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class OwnEx(Exception):
    def __init__(self, txt):
        self.txt = txt

class Data:
    day_month_year = '27062022'

    @classmethod
    def counter(cls):
        param = cls.day_month_year
        int(param)
        cls.day_month_year = param

    @staticmethod
    def stat_cl(numb):
        numb = str(numb)
        try:
            if int(numb[2: 4]) >= 12 or int(numb[2: 4]) <= 1:
                raise OwnEx(f'{numb} - bad month')
        except OwnEx as err:
            print(err)
        else:
            print(f'{numb} - date is good')
        finally:
            print(f'{numb} - finally')


a = Data()
print(a.__dict__, Data.__dict__)
print(a.day_month_year, type(a.day_month_year))
a.day_month_year = 23092019
a.example = 'one'

a.counter()

print(a.__dict__, Data.__dict__)
print(a.day_month_year, type(a.day_month_year))

Data.stat_cl(12002022)

