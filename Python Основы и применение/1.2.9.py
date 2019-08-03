"""
Реализуйте программу,
которая будет вычислять
количество различных объектов в списке.
Два объекта a и b
считаются различными,
если a is b равно False.

Вашей программе доступна переменная с названием objects,
которая ссылается на список, содержащий не более 100 объектов.
Выведите количество различных объектов в этом списке.
"""


a = [1, 2, 3, 4, 5, 1, 2, 3, True, True, False, 'a', 'a', 'c']

b = []

for i in a:
    if id(i) not in b:
        b.append(id(i))

print(len(b))

