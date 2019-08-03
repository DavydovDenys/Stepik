"""Напишите программу,
которая запускается из консоли
и печатает значения всех переданных
аргументов на экран (имя скрипта выводить не нужно).
Не изменяйте порядок аргументов при выводе.

Для доступа к аргументам командной строки
программы подключите модуль sys и используйте
переменную argv из этого модуля."""
from sys import argv

a = []
for i in argv[1:]:
    a.append(i)
for j in a:
    print(j, end=' ')
# ________________________или_такой вариант
# from sys import argv
# print(*sys.argv[1:])
