# Задача 3.1_1
"""
Вашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских букв.
За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.
Выведите одно число – минимальное число операций, после применения которых в строке s не останется вхождений строки
a, или Impossible, если операций потребуется более 1000.
"""
s, a, b = input(), input(), input()
if a not in s:
    print(0)
elif a in b:
    print('Impossible')
else:
    count = 0
    while a in s:
        s = s.replace(a, b)
        count += 1
    print(count)

# Задача 3.1_2
"""
Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s.

Пример:
s = "abababa"
t = "aba"

Вхождения строки t в строку s:
abababa
abababa
abababa
"""
# Задача 3.2_1
"""
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
"""
import re
import sys

pattern = r'cat.*cat'
for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line):
        print(line)

# Задача 3.2_2
"""
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве слова.
"""
import re
import sys

for line in sys.stdin:
    line = line.strip()
    if re.search(r"\bcat\b", line):
        print(line)

# Задача 3.2_3
"""
Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.
"""
import re
import sys

pattern = r'z.{3}z'
for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line):
        print(line)

# Задача 3.2_4
"""
Вам дана последовательность строк.
Выведите строки, содержащие обратный слеш "\﻿".
"""
import re
import sys

for line in sys.stdin:
    line = line.strip()
    if re.search(r'\B\\', line):
        print(line)

# Задача 3.2_5
"""
Вам дана последовательность строк.
Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).
"""
import re
import sys

for line in sys.stdin:
    line = line.strip()
    if re.search(r'\b(\w+)\1\b', line):
        print(line)

# Задача 3.2_6
"""
Вам дана последовательность строк.
В каждой строке замените все вхождения подстроки "human" на подстроку "computer"﻿ и выведите полученные строки.
"""
import re
import sys

for line in sys.stdin:
    line = line.strip()
    print(re.sub(r"human*", 'computer', line))

# Задача 3.2_7
"""
Вам дана последовательность строк.
В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" 
(регистр не важен), на слово "argh".
"""
import re
import sys

for line in sys.stdin:
    line = line.strip()
    print(re.sub(r'\b[a|A]+\b', 'argh', line, 1))

# Задача 3.2_8
"""
Вам дана последовательность строк.
В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
Буквой считается символ из группы \w.
"""
import re
import sys

for line in sys.stdin:
    print(re.sub(r'(\w)(\w)(\w|)', r'\2\1\3', line.strip()))

# Задача 3.2_9
"""
Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w.
"""
import re
import sys

for line in sys.stdin:
    print(re.sub(r'(\w)\1+', r'\g<1>', line.strip()))

# Задача 3.3_1
"""
Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, 
возможно с дополнительными параметрами внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за 
один переход и из C в B можно перейти за один переход.
Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.
Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.
"""
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

def selection_url(url_in):
    soup = BeautifulSoup(urlopen(url_in), 'html5lib')
    a_href_set = set()
    for link in soup.find_all('a'):
        a_href_set.add(link.get('href'))
    return a_href_set


url_a, url_b = input(), input()
check = False
for element in selection_url(url_a):
    if (requests.get(element).status_code == 200) and (url_b in selection_url(element)):
        print('Yes')
        check = True
        break
if not check:
    print('No')

# Задача 3.3_2
"""
Вашей программе на вход подается ссылка на HTML файл.
Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и вывести список сайтов, 
на которые есть ссылка. Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. 
"""
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

res = requests.get(input())
soup = BeautifulSoup(res.text, "lxml")

urls = set()
for link in soup.find_all('a'):
    urls.add(link.get('href'))

sites = set()
for url in urls:
    sites.add(urlparse(url).hostname)

sites.discard(None)
sites = sorted(sites)

for i in sites:
    print(i)

# Задача 3.4
"""
Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть 
поле name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.

Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.
<имя класса> : <количество потомков>
Выводить классы следует в лексикографическом порядке.
A : 3
B : 1
C : 2
"""
import json


def search(dic, parent):
    visited, stack = [], [parent]
    while stack:
        child = stack.pop()
        if child not in visited:
            visited.append(child)
            stack.extend(set(dic[child]) - set(visited))
    return visited
dictionary = {}
js_content = json.loads(input())
for i in js_content:
    dictionary[i['name']] = set()
    for j in i['parents']:
        dictionary[j] = set()
for i in js_content:
    for j in i['parents']:
        dictionary[j].add(i['name'])
res = [[0 for j in range(2)] for i in range(len(dictionary))]
i = 0
for par in dictionary:
    res[i][0] = par
    res[i][1] = len(search(dictionary, par))
    i += 1
for i in sorted(res):
    print(i[0], ':', i[1])

# Задача 3.5_1
"""
В этой задаче вам необходимо воспользоваться API сайта numbersapi.com
Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом 
числе.

Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.
"""
import requests


with open('dataset.txt') as f:
    read = f.read().splitlines()

for x in read:
    res = requests.get(f'http://numbersapi.com/{x}/math?json=true')
    if res.json()['found']:
        print('Interesting')
    else:
        print('Boring')

# Задача 3.5_2
"""
В этой задаче вам необходимо воспользоваться API сайта artsy.net
В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).
Вам даны идентификаторы художников в базе Artsy.
Для каждого идентификатора получите информацию о имени художника и годе рождения.
"""
import requests

api_url = 'https://api.artsy.net/api/artists/{}'

headers = {
    "X-Xapp-Token":12345
}

artists = []

with open('dataset_24476_4.txt') as f:
    for line in f:
        artist_id = line.rstrip()
        res = requests.get(api_url.format(artist_id), headers=headers)
        if res.status_code == 200:
            #print(res.json()['birthday'], res.json()['sortable_name'])
            artists.append([res.json()['birthday'], res.json()['sortable_name']])

artists.sort()

for artist in artists:
    print(artist[1])

# Задача 3.6
"""
Вам дано описание пирамиды из кубиков в формате XML.
Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue﻿).
Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.
Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1. 
Кубики, расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками, 
имеют ценность 3. И т. д.
Ценность цвета равна сумме ценностей всех кубиков этого цвета.
Выведите через пробел три числа: ценности красного, зеленого и синего цветов.
"""
from xml.etree import ElementTree


def cubes(xml_tree, dep):
    colors[xml_tree.attrib['color']] += dep
    for elem in xml_tree:
        cubes(elem, dep + 1)


colors = {'red': 0, 'green': 0, 'blue': 0}
tree = ElementTree.fromstring(input())
cubes(tree, 1)
print(*colors.values())