"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над четвертым заданием.
Разработать методы, отвечающие за приём оргтехники на
склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и
количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над пятым заданием. Р
еализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class NumCheck(Exception):
    def __init__(self, txt):
        self.txt = txt


class Store:
    x = 0

    def __init__(self, pid=0, number=0):
        self.pid = Store.x
        self.number = number


    @classmethod
    def getting_eq(cls, **kwargs):
        dic = {**kwargs}
        Store.x = Store.x + 1
        dic['pid'] = cls.x
        new_pri = Device(**dic)
        print('this is classmethod -', new_pri.__dict__, new_pri)


class Equipment(Store):
    def __init__(self, department, price, pid, number):
        super().__init__(pid, number)
        self.price = price
        self.department = department


class Device(Equipment):
    def __init__(self, department, price, pid, number, owner, color):
        super().__init__(department, price, pid, number)
        self.owner = owner
        self.color = color
        self.check()

    def check(self):
        try:
            if type(self.number) != 'int':
                raise NumCheck(f'{type(self.number), self.number} the number should be int')
        except NumCheck as err:
            print(err)
        else:
            print(f'{type(self.number), self.number} the number is int')


printer = Device(department='policy', price=1000, pid=0, number='0', owner='ghost', color='black')
computer = Device(department='emergency', price=3000, pid=0, number=0, owner='photo', color='black')
xerox = Device(department='office', price=6000, pid=0, number=0, owner='host', color='red')

Store.getting_eq(department='strike', price=60,  number=3, owner='ghost', color='black')
Store.getting_eq(department='bike', price=60,  number=3, owner='lacost', color='black')
Store.getting_eq(department='nike', price=60,  number=3, owner='jsd', color='black')

new = Device(department='sell', price=7000, pid=30, number=100, owner='lok', color='black')
print(printer.__dict__, computer.__dict__, xerox.__dict__, new.__dict__, sep='\n')
