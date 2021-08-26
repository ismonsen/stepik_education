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
    print(re.sub(r'human*', 'computer', line))

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

"""
Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w.
"""
import re
import sys

for line in sys.stdin:
    print(re.sub(r'(\w)\1+', r'\g<1>', line.strip()))