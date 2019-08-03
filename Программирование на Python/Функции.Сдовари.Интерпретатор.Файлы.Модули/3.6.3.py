"""
Имеется набор файлов,
каждый из которых, кроме последнего,
содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл.
В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.
"""

import requests
with open('./dataset_3378_4.txt', 'r', encoding='utf-8') as pdf:
    n = pdf.read().replace('\n', '').split()
    print(n)
r = requests.get(*n)
print(r)
s = r.text
print(s)
while 'We' not in s:
    r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + s)
    s = r.text
    print(s)
with open('./dataset_3378_4_wr.txt', 'w') as owr:
    owr.write(s)
