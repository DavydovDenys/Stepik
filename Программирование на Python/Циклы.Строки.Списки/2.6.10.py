"""
Напишите программу,
на вход которой подаётся прямоугольная
матрица в виде последовательности строк,
заканчивающихся строкой, содержащей только строку "end" (без кавычек)

Программа должна вывести матрицу того же размера,
у которой каждый элемент в позиции i, j
 равен сумме элементов первой матрицы на позициях
 (i-1, j), (i+1, j), (i, j-1), (i, j+1).
 У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент
сам себе является соседом по соответствующему направлению.

Sample Input 1:

9 5 3
0 7 -1
-5 2 9
end
Sample Output 1:

3 21 22
10 6 19
20 16 -1
Sample Input 2:

1
end
Sample Output 2:

4
"""

lst = []
while True:
    n = input()
    if n == 'end':
        break
    lst.append([int(s) for s in n.split()])


lst2 = []
count2 = 0
for i in range(len(lst)):
    lst2.append([])
    if i < len(lst) - 1:
        for j in range(len(lst[i])):
            if j < len(lst[i]) - 1:
                lst2[count2].append(int(lst[i][j + 1]) + int(lst[i][j - 1]) + int(lst[i + 1][j]) + int(lst[i - 1][j]))
            if j == len(lst[i]) - 1:
                lst2[count2].append(int(lst[i][j - 1]) + int(lst[i][0]) + int(lst[i + 1][j]) + int(lst[i - 1][j]))
    if i == len(lst) - 1:
        for j in range(len(lst[i])):
            if j < len(lst[i]) - 1:
                lst2[count2].append(int(lst[i][j + 1]) + int(lst[i][j - 1]) + int(lst[0][j]) + int(lst[i - 1][j]))
            if j == len(lst[i]) - 1:
                lst2[count2].append(int(lst[i][0]) + int(lst[i][j - 1]) + int(lst[0][j]) + int(lst[i - 1][j]))
    count2 += 1

for i in lst2:
    for j in i:
        print(j, end=' ')
    print()

