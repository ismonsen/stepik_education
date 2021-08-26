# Задача 1.1
# Реализуйте программу, которая принимает последовательность чисел и выводит их сумму.
res = 0
for i in range(int(input())):
    res += int(input())
print(res)

# Задача 1.2
"""
Реализуйте программу, которая будет вычислять количество различных объектов в списке.
Два объекта a и b считаются различными, если a is b равно False. На вход подается список
"""
objects = [1, 2, 1, 3, 4, 5]  # input
a = []
for i in objects:
    if i not in a:
        a.append(i)
print(len(a))

# Задача 1.3_1
"""
Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента целое число 
x и возвращающую самое маленькое целое число y, такое что:
y больше или равно x
y делится нацело на 5
"""


def closest_mod_5(x):
    if x % 5 != 0:
        x += 5 - (x % 5)
    return x


# Задача 1.3_2
"""
Сочетанием из n элементов по k называется подмножество этих n элементов размера k.
Два сочетания называются различными, если одно из сочетаний содержит элемент, который не содержит другое.
Числом сочетаний из n по k называется количество различных сочетаний из n по k. Обозначим это число за C(n, k).
Пусть n = 3, т. е. есть три элемента (1, 2, 3). Пусть k = 2.
Все различные сочетания из 3 элементов по 2: (1, 2), (1, 3), (2, 3).
Различных сочетаний три, поэтому C(3, 2) = 3. Несложно понять, что C(n, 0) = 1, так как из n элементов выбрать 
0 можно единственным образом, а именно, ничего не выбрать. Также несложно понять, что если k > n, то C(n, k) = 0, 
так как невозможно, например, из трех элементов выбрать пять.
Для вычисления C(n, k) в других случаях используется следующая рекуррентная формула:
C(n, k) = C(n - 1, k) + C(n - 1, k - 1).
Реализуйте программу, которая для заданных n и k вычисляет C(n, k).
Вашей программе на вход подается строка, содержащая два целых числа n и k (1 ≤ n ≤ 10, 0 ≤ k ≤ 10).
Ваша программа должна вывести единственное число: C(n, k).
"""
n, k = map(int, input().split())


def new(nn, kk):
    if kk == 0:
        return 1
    elif kk > nn:
        return 0
    else:
        return new(nn - 1, kk) + new(nn - 1, kk - 1)


print(new(n, k))

# Задача 1.4
"""
Реализуйте программу, которая будет эмулировать работу с пространствами имен. 
Необходимо реализовать поддержку создания пространств имен и добавление в них переменных.
create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
add <namespace> <var> – добавить в пространство <namespace> переменную <var>
get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из пространства 
<namespace>, или None, если такого пространства не существует
"""


def add_sp(diction, name_space, argument):
    if name_space not in diction:
        diction[name_space] = {}
        diction[name_space]['vars'] = []
        diction[name_space]['vars'].append(argument)
    else:
        diction[name_space]['vars'].append(argument)


def create_sp(diction, name_space, parent):
    if name_space not in diction:
        diction[name_space] = {}
        diction[name_space]['vars'] = []
        diction[name_space]['parent'] = parent


def get_sp(diction, name_space, argument):
    if argument in diction[name_space]['vars']:
        return name_space
    else:
        upper_name_space = diction[name_space]['parent']
        if upper_name_space is None:
            return None
        else:
            return get_sp(diction, upper_name_space, argument)


dic = {'global': {'vars': [], 'parent': None}}
for i in range(int(input())):
    cmd, name_sp, arg = input().split()
    if cmd == 'add':
        add_sp(dic, name_sp, arg)
    elif cmd == 'create':
        create_sp(dic, name_sp, arg)
    elif cmd == 'get':
        print(get_sp(dic, name_sp, arg))

# Задача 1.5_1
"""
Реализуйте класс MoneyBox, для работы с виртуальной копилкой.
Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет, которые можно 
положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке, предоставлять возможность 
добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё какое-то количество монет, не превышая 
ее вместимость.
"""


class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity

    def can_add(self, v):
        if self.capacity >= v:
            return True
        else:
            return False

    def add(self, v):
        if self.can_add(v):
            self.capacity -= v


# Задача 1.5_2
"""
Вам дается последовательность целых чисел и вам нужно ее обработать и вывести на экран сумму первой пятерки чисел 
из этой последовательности, затем сумму второй пятерки, и т. д.
"""


class Buffer:
    def __init__(self):
        self.massive = []

    def add(self, *p):
        self.massive += p
        while len(self.massive) >= 5:
            print(sum(self.massive[0:5]))
            del self.massive[0:5]

    def get_current_part(self):
        return self.massive


# Задача 1.6_1
"""
Вам дано описание наследования классов в следующем формате.
<имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.
На вход подается количество строк, описание наследования классов
Затем количество строк с двумя классами - является ли 1й предком 2го
Вывод - Yes / No
"""


def search(child, parent):
    if child == parent:
        return True
    for p in dictionary[child]:
        if search(p, parent):
            return True
    return False


son = ''
dictionary = {}
for i in range(int(input())):
    s = input().replace(':', '').split()
    if len(s) == 1:
        dictionary[s[0]] = []
    else:
        son = s.pop(0)
        if son not in dictionary:
            dictionary[son] = []
        for j in s:
            dictionary[son].append(j)
    s.clear()
for _ in range(int(input())):
    A, B = input().split()
    print("Yes" if search(B, A) else "No")

# Задача 1.6_2
"""
Реализуйте структуру данных, представляющую собой расширенную структуру стек. Необходимо поддерживать 
добавление элемента на вершину стека, удаление с вершины стека, и необходимо поддерживать операции 
сложения, вычитания, умножения и целочисленного деления. Операция сложения на стеке определяется следующим образом. 
Со стека снимается верхний элемент (top1), затем снимается следующий верхний элемент (top2), и затем как результат 
операции сложения на вершину стека кладется элемент, равный top1 + top2. Аналогичным образом определяются операции 
вычитания (top1 - top2), умножения (top1 * top2) и целочисленного деления (top1 // top2).
Реализуйте эту структуру данных как класс ExtendedStack, отнаследовав его от стандартного класса list.
"""


class ExtendedStack(list):

    def sum(self):
        self.append(self.pop() + self.pop())

    def sub(self):
        self.append(self.pop() - self.pop())

    def mul(self):
        self.append(self.pop() * self.pop())

    def div(self):
        self.append(self.pop() // self.pop())


# Задача 1.6_3
"""
Реализуйте класс LoggableList, отнаследовав его от классов list и Loggable таким образом, чтобы при добавлении элемента 
в список посредством метода append в лог отправлялось сообщение, состоящее из только что добавленного элемента.
Ваша программа не должна содержать класс Loggable. При проверке вашей программе будет доступен этот класс, 
и он будет содержать метод log, описанный выше.
"""
import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, number):
        self.extend([number])
        self.log(number)
