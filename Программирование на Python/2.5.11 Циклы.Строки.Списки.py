"""
Напишите программу,
которая принимает на вход список чисел в одной строке
и выводит на экран в одну строку значения,
которые повторяются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться,
порядок их вывода может быть произвольным.

Sample Input 1:

4 8 0 3 4 2 0 3
Sample Output 1:

0 3 4
Sample Input 2:

10
Sample Output 2:

Sample Input 3:

1 1 2 2 3 3
Sample Output 3:

1 2 3
Sample Input 4:

1 1 1 1 1 2 2 2
Sample Output 4:

1 2
"""

s = [int(i) for i in input().split()]
t = []
s.sort()
l = len(s) - 1
k = 100000
if len(s) != 1:
    for i in range(0, l):
        if s[i] == s[i + 1] and s[i] != k:
            t.append(s[i])
            k = s[i]
    for j in range(l, l + 1):
        if s[-1] == s[-2] and s[j] != k:
            t.append(s[j])
n = len(t)
for g in range(0, n):
    print(t[g], end=' ')
