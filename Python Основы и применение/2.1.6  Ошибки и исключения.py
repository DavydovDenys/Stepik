"""
Вашей программе будет доступна функция foo,
которая может бросать исключения.

Вам необходимо написать код,
который запускает эту функцию,
затем ловит исключения ArithmeticError,
AssertionError, ZeroDivisionError и выводит имя пойманного исключения.

Пример решения, которое вы должны отправить на проверку.

try:
    foo()
except Exception:
    print("Exception")
except BaseException:
    print("BaseException")
"""

try:
    2/0
except ZeroDivisionError:
    print('ZeroDivisionError')
except ArithmeticError:
    print('ArithmeticError')
except AssertionError:
    print('AssertionError')
