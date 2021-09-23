# Задача 8_7.1
"""
На вход программе подаются два числа. Напишите программу, определяющую, есть ли в данных числах одинаковые цифры.
"""
set1, set2 = set(int(_) for _ in input()), set(int(_) for _ in input())
if len(set1 & set2) > 0:
    print('YES')
else:
    print('NO')

# Задача 8_7.2
"""
На вход программе подаются два числа. Напишите программу, которая определяет, входят ли в запись первого числа все 
цифры, содержащиеся в записи второго (независимо от повтора, то есть количества цифр) числа или нет.
"""
print(['NO', 'YES'][set(input()).issuperset(set(input()))])

# Задача 8_7.3
"""
Даны по 10-балльной шкале оценки по информатике трех учеников. Напишите программу, которая выводит множество оценок, 
которые есть и у первого и у второго учеников, но которых нет у третьего ученика.
"""
set1 = set(int(_) for _ in input().split())
set2 = set(int(_) for _ in input().split())
set3 = set(int(_) for _ in input().split())
print(*sorted(set1 & set2 - set3, reverse=True))

# Задача 8_7.4
"""
Даны по 10-балльной шкале оценки по математике трех учеников. Напишите программу, которая выводит множество оценок, 
имеющихся у учеников, которые встречаются не более, чем у двух из указанных учеников.
"""
set1 = set(int(_) for _ in input().split())
set2 = set(int(_) for _ in input().split())
set3 = set(int(_) for _ in input().split())
print(*sorted((set1 | set2 | set3) - (set1 & set2 & set3)))

# Задача 8_7.5
"""
Даны по 10-балльной шкале оценки по физике трех учеников. Напишите программу, которая выводит множество оценок третьего 
ученика, которые не встречаются ни у первого, ни у второго ученика.
"""
set1 = set(int(_) for _ in input().split())
set2 = set(int(_) for _ in input().split())
set3 = set(int(_) for _ in input().split())
print(*sorted(set3 - (set1 | set2), reverse=True))

# Задача 8_7.6
"""
Даны по 10-балльной шкале оценки по биологии трех учеников. Напишите программу, которая выводит множество оценок, 
не встречающихся ни у одного из трех учеников.
"""
digits = set(range(11))
set1 = set(int(_) for _ in input().split())
set2 = set(int(_) for _ in input().split())
set3 = set(int(_) for _ in input().split())
print(*sorted(digits - (set1 | set2 | set3)))

# Задача 8_8.1
"""
Используя генератор множеств, дополните приведенный код, так чтобы получить множество, содержащее уникальные значения 
списка items. Результат вывести на одной строке, в упорядоченном виде, разделяя элементы одним символом пробела.
"""
items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
digits = {int(d) for d in items}
print(*sorted(digits))

# Задача 8_8.2
"""
Используя генератор множеств, дополните приведенный код, так чтобы получить множество, содержащее первую букву каждого
слова (в нижнем регистре) списка words. Результат вывести на одной строке в алфавитном порядке, разделяя элементы одним 
символом пробела.
"""
words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon',
         'tangerine', 'Watermelon', 'currant', 'Almond']
my_set = {i[0].lower() for i in words}
print(*sorted(my_set))

# Задача 8_8.3
"""
Используя генератор множеств, дополните приведенный код, так чтобы получить множество, содержащее уникальные слова 
(в нижнем регистре) строки sentence. Результат вывести на одной строке в алфавитном порядке, разделяя элементы одним 
символом пробела.
"""
sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, 
save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, 
over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, 
you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered 
and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges. '''
words = [word.lower().strip('.,;():-?!') for word in sentence.split()]
print(*sorted(set(words)))

# Задача 8_8.4
"""
Используя генератор множеств, дополните приведенный код, так чтобы получить множество, содержащее уникальные слова  
строки sentence длиною меньше 44 символов. Результат вывести на одной строке (в нижнем регистре) в алфавитном порядке, 
разделяя элементы одним символом пробела.
"""
sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, 
save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, 
over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, 
you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered 
and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges. '''
words = [word.lower().strip('.,;():-?!') for word in sentence.split()]
my_set = {word for word in words if len(word) < 4}
print(*sorted(my_set))

# Задача 8_8.5
"""
Используя генератор множеств, дополните приведенный код, так чтобы он выбрал из списка files уникальные имена файлов 
c расширением .png, независимо от регистра имен и расширений. Имена файлов вывести вместе с расширением, все на одной 
строке, в нижнем регистре, в алфавитном порядке через пробел.
"""
files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT',
         'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py',
         'stepik.org', 'kotlin.ko', 'github.git']
my_set = {word.lower() for word in files if '.png' in word.lower()}
print(*sorted(my_set))