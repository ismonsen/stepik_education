# Задача 2.1_1
# Вашей программе будет доступна функция foo, которая может бросать исключения.
# Вам необходимо написать код, который запускает эту функцию, затем ловит исключения ArithmeticError, AssertionError,
# ZeroDivisionError и выводит имя пойманного исключения.
# Пример решения, которое вы должны отправить на проверку.


def foo():
    pass


try:
    foo()
except ZeroDivisionError:
    print("ZeroDivisionError")
except AssertionError:
    print("AssertionError")
except ArithmeticError:
    print("ArithmeticError")

# Задача 2.1_2
"""
В первой строке входных данных содержится целое число n - число классов исключений.
В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется 
i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется 
сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.
В следующей строке содержится число m - количество обрабатываемых исключений.
Следующие m строк содержат имена исключений в том порядке, в каком они были написаны у Антона в коде.
Гарантируется, что никакое исключение не обрабатывается дважды.
"""


def searching(comm):
    if comm in s1:
        return comm
    elif comm in dictionary:
        for par in dictionary[comm]:
            if searching(par):
                return comm


dictionary = {}
for _ in range(int(input())):
    s = input().replace(':', '').split()
    dictionary[s[0]] = [] if len(s) == 1 else s[1:]
s1 = set()
tem = ''
for i in range(int(input())):
    tem = input()
    if searching(tem):
        print(searching(tem))
    s1.add(tem)
# Задача 2.1_3
"""
Реализуйте класс PositiveList, отнаследовав его от класса list, для хранения положительных целых чисел.
Также реализуйте новое исключение NonPositiveError. В классе PositiveList переопределите метод append(self, x) 
таким образом, чтобы при попытке добавить неположительное целое число бросалось исключение NonPositiveError и 
число не добавлялось, а при попытке добавить положительное целое число, число добавлялось бы как в стандартный list.
"""


class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, x):
        if x > 0:
            self += [x]
        else:
            raise NonPositiveError()


# Задача 2.2
"""
В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
Во второй строке дано одно число days -- число дней.
Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента 
исходной даты date пройдет число дней, равное days.
"""
import datetime

args = [int(i) for i in input().split()]
days = datetime.timedelta(int(input()))
data = datetime.date(*args) + days
print(data.strftime("%Y %-m %-d"))

# Задача 2.3_1
"""
Одним из самых часто используемых классов в Python является класс filter. Он принимает в конструкторе два аргумента 
a и f – последовательность и функцию, и позволяет проитерироваться только по таким элементам x из последовательности a, 
что f(x) равно True. Будем говорить, что в этом случае функция f допускает элемент x, а элемент x является допущенным.
В данной задаче мы просим вас реализовать класс multifilter, который будет выполнять ту же функцию, что и стандартный 
класс filter, но будет использовать не одну функцию, а несколько.
"""


class multifilter:
    def judge_half(pos, neg):
        return pos >= neg

    def judge_any(pos, neg):
        return pos >= 1

    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.index = 0
        self.judge = judge

    def __iter__(self):
        while self.index < len(self.iterable):
            pos = 0
            neg = 0
            for f in self.funcs:
                if f(self.iterable[self.index]):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                yield self.iterable[self.index]
            self.index += 1
        else:
            raise StopIteration


def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


# Задача 2.3_2
"""
Целое положительное число называется простым, если оно имеет ровно два различных делителя, 
то есть делится только на единицу и на само себя.
Реализуйте функцию-генератор primes, которая будет генерировать простые числа в порядке возрастания, начиная с числа 2.
"""
from math import factorial as fac


def primes():
    yield 2
    x = 3
    while True:
        if (fac(x - 1) + 1) % x == 0:
            yield x
        x += 1


# Задача 2.4
"""
Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.
"""
lines = open("input.txt").readlines()
with open("output.txt", "w") as out:
    out.writelines(reversed(lines))

# Задача 2.5
"""
Реализуйте функцию mod_checker(x, mod=0), которая будет генерировать лямбда функцию от одного аргумента y, 
которая будет возвращать True, если остаток от деления y на x равен mod, и False иначе.
"""


def mod_checker(x, mod=0):
    return lambda y: y % x == mod
