"""
Вам дано описание наследования классов в следующем формате.
<имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.

Или эквивалентно записи:

class Class1(Class2, Class3 ... ClassK):
    pass
Класс A является прямым предком класса B, если B отнаследован от A:


class B(A):
    pass


Класс A является предком класса B, если
A = B;
A - прямой предок B
существует такой класс C, что C - прямой предок B и A - предок C

Например:
class B(A):
    pass

class C(B):
    pass

# A -- предок С


Вам необходимо отвечать на запросы, является ли один класс предком другого класса

Важное примечание:
Создавать классы не требуется.
Мы просим вас промоделировать этот процесс,
и понять существует ли путь от одного класса до другого.
Формат входных данных
В первой строке входных данных содержится целое число
n - число классов.

В следующих n строках содержится описание наследования классов.
В i-й строке указано от каких классов наследуется i-й класс.
Обратите внимание, что класс может ни от кого не наследоваться.
Гарантируется, что класс не наследуется сам от себя (прямо или косвенно),
что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число q - количество запросов.

В следующих q строках содержится описание запросов в формате
<имя класса 1> <имя класса 2>.
Имя класса – строка, состоящая из символов латинского алфавита,
длины не более 50.

Формат выходных данных
Для каждого запроса выведите в отдельной строке слово "Yes",
если класс 1 является предком класса 2, и "No", если не является.

Sample Input:

4
A
B : A
C : A
D : B C
4
A B
B D
C D
D A
Sample Output:

Yes
Yes
Yes
No
"""


classes = {}


def create_class(class_name, parents, dict_of_classes=classes):
    """
    Функция создает словарь ключ/значение,где ключ - это родительский класс,
    значение - список с одним или несколькими значениями родительских классов
    :param class_name:
    :param parents:
    :param dict_of_classes:
    :return:
    """
    if parents not in classes.keys():
        # если родителя нету,создаем ключ с его именем
        # с пустым списком в качестве значения
        classes[parents] = []
        # добавляем дочерний класс в список родителя
        classes[parents].append(class_name)
    elif parents in classes.keys():
        # если родитель существует
        # добавляем в его список дочерний класс
        classes[parents].append(class_name)


def find_path(parents, sub_, dict_of_classes=classes):
    """
    Функция проверяет является ли parents родительским классом
    класса sub_class.
    В первую очередь проверяется существование ключа parents в словаре,
    если такого ключа не существует,значит класс не является родительским,
    функция прекращает свою работу.
    Далее идет проверка на нахождение sub_class среди значений ключа parents,если
    верно,тогда вернуть parents
    Когда sub_class отсутствует среди значений ключа parents,
    идет проверка каждого значения parents на статус родительского класса -
    является ли значение ключом словаря classes.
    Если класс - родительский,проверяем нахождение sub_class среди значений
    :param parents:
    :param sub_:
    :param dict_of_classes:
    :return:
    """
    if parents == sub_:
        return parents
    elif parents not in classes.keys():
        return None
    elif sub_class in classes[parents]:
        return parents
    elif sub_class not in classes[parents]:
        for parent in classes[parents]:
            if parent not in classes.keys():
                continue
            elif sub_class in classes[parent]:
                return parent
            else:
                continue
        return None


def answer(parents, sub_class):
    if find_path(parents, sub_class):
        print('Yes')
    else:
        print('No')


a = []
n = int(input())
for i in range(n):
    i = input().split()
    a.append(i)

for j in range(len(a)):
    if len(a[j]) == 1:
        sub = a[j][0]
        super_class = sub
        create_class(sub, super_class)
    elif len(a[j]) == 3:
        sub = a[j][0]
        super_class = a[j][2]
        create_class(sub, super_class)
    elif len(a[j]) > 3:
        sub = a[j][0]
        for element in a[j][2:]:
            super_class = element
            create_class(sub, super_class)

b = []

q = int(input())
for _q in range(q):
    question = input().split()
    b.append(question)

for y in range(len(b)):
    if b[y][0] == b[y][1]:

        super_class = b[y][0]
        sub_class = b[y][1]
        answer(super_class, sub_class)
    else:
        super_class = b[y][0]
        sub_class = b[y][1]
        answer(super_class, sub_class)


