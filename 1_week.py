# Задача 1.8_1
# Тимофей обычно спит ночью XX часов и устраивает себе днем тихий час на YY минут.
# Определите, сколько всего минут Тимофей спит в сутки.
x, y = int(input()), int(input())
print(x * 60 + y)

# Задача 1.8_2
# Коля каждый день ложится спать ровно в полночь и недавно узнал, что оптимальное время для его сна
# составляет XX минут. Коля хочет поставить себе будильник так, чтобы он прозвенел ровно через XX минут
# после полуночи, однако для этого необходимо указать время сигнала в формате часы, минуты.
# Помогите Коле определить, на какое время завести будильник.
a = input()
b = int(a) // 60
c = int(a) % 60
print(b)
print(c)

# Задача 1.8_3
# Катя узнала, что ей для сна надо XX минут. В отличие от Коли, Катя ложится спать после полуночи
# в HH часов и MM минут. Помогите Кате определить, на какое время ей поставить будильник, чтобы
# он прозвенел ровно через XX минут после того, как она ляжет спать.
a, b, c = int(input()), int(input()), int(input())
e = a % 60 + c % 60
d = a // 60 + b + e // 60
e = e % 60
print(d)
print(e)

# Задача 1.10_1
# Из передачи “Здоровье” Аня узнала, что рекомендуется спать хотя бы AA часов в сутки, но пересыпать тоже вредно
# и не стоит спать более BB часов. Сейчас Аня спит HH часов в сутки. Если режим сна Ани удовлетворяет рекомендациям
# передачи “Здоровье”, выведите “Это нормально”. Если Аня спит менее AA часов, выведите “Недосып”, если же более
# BB часов, то выведите “Пересып”.
# Получаемое число AA всегда меньше либо равно BB.
# На вход программе в три строки подаются переменные в следующем порядке: AA, BB, HH.
A, B, H = int(input()), int(input()), int(input())
if (H <= B) and (H >= A):
    print('Это нормально')
elif H < A:
    print("Недосып")
else:
    print("Пересып")

# Задача 1.10_2
# Требуется определить, является ли данный год високосным.
y = int(input())
if (y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0):
    print('Високосный')
else:
    print('Обычный')

# Задача 1.12_1
# Напишите программу, вычисляющую площадь треугольника по переданным длинам трёх его сторон по формуле Герона
a, b, c = int(input()), int(input()), int(input())
p = (a + b + c) / 2
S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(S)

# Задача 1.12_2
# Напишите программу, принимающую на вход целое число, которая выводит True, если переданное
# значение попадает в интервал
# put your python code here
a = int(input())
if (12 >= a > -15) or (17 > a > 14) or (a >= 19):
    print("True")
else:
    print("False")

# Задача 1.12_3
# Напишите простой калькулятор (+, -, /, *, mod, div, pow)
a, b, oper = float(input()), float(input()), input()
if oper == '+':
    print(a + b)
elif oper == '-':
    print(a - b)
elif oper == '*':
    print(a * b)
elif oper == 'pow':
    print(a ** b)
elif b == 0:
    print('Деление на 0!')
elif oper == 'div':
    print(a // b)
elif oper == '/':
    print(a / b)
elif oper == 'mod':
    print(a % b)

# Задача 1.12_4
# Вычисление площади по фигуре
s = input()
if s == 'прямоугольник':
    a, b = float(input()), float(input())
    print(a * b)
elif s == 'треугольник':
    a, b, c = float(input()), float(input()), float(input())
    p = (a + b + c) / 2
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
else:
    r = int(input())
    print(float(3.14 * r * r))

# Задача 1.12_5
# Напишите программу, которая получает на вход три целых числа, по одному числу в строке,
# и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.
a, b, c = int(input()), int(input()), int(input())
if a > b > c:
    print(a)
    print(c)
    print(b)
elif b > c > a:
    print(b)
    print(a)
    print(c)
elif a > c > b:
    print(a)
    print(b)
    print(c)
elif b > a > c:
    print(b)
    print(c)
    print(a)
elif c > b > a:
    print(c)
    print(a)
    print(b)
elif c > a > b:
    print(c)
    print(b)
    print(a)
elif a == b > c:
    print(a)
    print(c)
    print(b)
elif b == c > a:
    print(b)
    print(a)
    print(c)
elif c == a > b:
    print(a)
    print(b)
    print(c)
elif a == b < c:
    print(c)
    print(a)
    print(b)
elif b == c < a:
    print(a)
    print(b)
    print(c)
elif c == a < b:
    print(b)
    print(a)
    print(c)
else:
    print(a)
    print(b)
    print(c)

# Задача 1.12_6
# Вывести правильное слова "программист" при вводе числа
s = input()
x = len(s)
if s == '1':
    print(s, ' программист')
elif s[x-1] == '1' and s[x-2] != '1':
    print(s, ' программист')
elif s[x-2] == '1' and s[x-1] == '2':
    print(s, ' программистов')
elif s[x-2] == '1' and s[x-1] == '3':
    print(s, ' программистов')
elif s[x-2] == '1' and s[x-1] == '4':
    print(s, ' программистов')
elif s[x-1] == '2' or s[x-1] == '3' or s[x-1] == '4':
    print(s, ' программиста')
elif s[x-2] == '1' and s[x-1] == '1':
    print(s, ' программистов')
else:
    print(s, ' программистов')

# Задача 1.12_7
# На вход программе подаётся строка из шести цифр.
# Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.
s = input()
if int(s[0]) + int(s[1]) + int(s[2]) == int(s[3]) + int(s[4]) + int(s[5]):
    print('Счастливый')
else:
    print('Обычный')

