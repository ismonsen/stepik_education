# Задача 4_6.1
"""
На вход программе подаются два натуральных числа n и m. Напишите программу для создания матрицы размером n×m, заполнив
её символами . и * в шахматном порядке. В левом верхнем углу должна стоять точка. Выведите полученную матрицу на экран,
разделяя элементы пробелами.
"""
n, m = input().split()
for i in range(int(n)):
    if i % 2 == 0:
        for j in range(int(m)):
            if j % 2 == 0:
                print('.', end=' ')
            else:
                print('*', end=' ')
    else:
        for x in range(int(m)):
            if x % 2 > 0:
                print('.', end=' ')
            else:
                print('*', end=' ')
    print()

# Задача 4_6.2
"""
На вход программе подается натуральное число nn. Напишите программу, которая создает матрицу размером n×n 
и заполняет её по следующему правилу:
числа на побочной диагонали равны 1;
числа, стоящие выше этой диагонали, равны 0;
числа, стоящие ниже этой диагонали, равны 2
"""
n = int(input())
a = [[2] * n for i in range(n)]
for i in range(n):
    for j in range(n - i):
        a[i][j] = 0
    a[i][n - i - 1] = 1
for line in a:
    print(*line)

# Задача 4_6.3
"""
На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m 
и заполняет её числами от 1 до n*m в соответствии с образцом. 
3 4 ->>>
1  2  3  4
5  6  7  8
9  10 11 12
"""
n, m = (int(i) for i in input().split())
number = 1
for i in range(n):
    for j in range(m):
        print(str(number).ljust(3), end='')
        number += 1
    print()

# Задача 4_6.4
"""
На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m 
и заполняет её числами от 1 до n*m в соответствии с образцом. 
3 7 ->>>
1  4  7  10 13 16 19
2  5  8  11 14 17 20
3  6  9  12 15 18 21
"""


def counter():
    global c
    c += 1
    return c


c = 0
n, m = (int(i) for i in input().split())
a = [[counter() for i in range(n)] for j in range(m)]
for i in range(n):
    for j in range(m):
        print(str(a[j][i]).ljust(3), end='')
    print()

# Задача 4_6.5
"""
На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n в соответствии 
с образцом. 
5 - >>>
1  0  0  0  1
0  1  0  1  0
0  0  1  0  0
0  1  0  1  0
1  0  0  0  1
"""
n = int(input())
a = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    a[i][n - i - 1] = 1
    a[i][i] = 1
    for j in range(n):
        print(str(a[i][j]).ljust(3), end='')
    print()

# Задача 4_6.6
"""
На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n в соответствии 
с образцом.
5 ->>>
1  1  1  1  1
0  1  1  1  0
0  0  1  0  0
0  1  1  1  0
1  1  1  1  1
"""
n = int(input())
for i in range(n):
    for j in range(n):
        if (i <= j and i <= n - 1 - j) or (i >= j and i >= n - 1 - j):
            print('1'.ljust(3), end='')
        else:
            print('0'.ljust(3), end='')
    print()

# Задача 4_6.7
"""
На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m 
и заполняет в соответствии с образцом.
5 5 ->>
1 2 3 4 5
2 3 4 5 1
3 4 5 1 2
4 5 1 2 3
5 1 2 3 4
"""
n, m = [int(i) for i in input().split()]
a = [x + 1 for x in range(m)]
for i in range(n):
    i = i % m
    print(*a[i:], *a[0:(m - i) * -1])

# Задача 4_6.8
"""
На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m 
и заполнив её "змейкой" в соответствии с образцом.
3 5 ->>
1  2  3  4  5
10 9  8  7  6
11 12 13 14 15
"""


def counter():
    global c
    c += 1
    return c


c = 0
n, m = map(int, input().split())
a = [[counter() for j in range(m)] for i in range(n)]
for i in range(n):
    if i % 2 == 1:
        print(*a[i][::-1])
    else:
        print(*a[i])

# Задача 4_6.9
"""
На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m 
и заполнив её "диагоналями" в соответствии с образцом.
3 5 ->>
1  2  4  7  10
3  5  8  11 13
6  9  12 14 15
"""
n, m = map(int, input().split())
matrix = [[0] * m for _ in range(n)]
counter = 1
for x in range(n + m):
    for i in range(n):
        for j in range(m):
            if i + j == x:
                matrix[i][j] = counter
                counter += 1
for row in range(n):
    for col in range(m):
        print(str(matrix[row][col]).ljust(3), end='')
    print()

# Задача 4_6.10
"""
На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m 
и заполнив её "спиралью" в соответствии с образцом
4 5 ->>>
1  2  3  4  5
14 15 16 17 6
13 20 19 18 7
12 11 10 9  8
"""
n, m = map(int, input().split())
matrix = [[0] * m for _ in range(n)]
i, j, x = 0, 0, 1
ai_0, aj_0, ai_n, aj_m = 1, 0, n - 1, m - 1
while x <= n * m:
    while j <= aj_m:
        if matrix[i][j] == 0:
            matrix[i][j] = x
        x += 1
        j += 1
    else:
        j = aj_m
        aj_m -= 1
        i += 1
    while i <= ai_n:
        if matrix[i][j] == 0:
            matrix[i][j] = x
        x += 1
        i += 1
    else:
        i = ai_n
        ai_n -= 1
        j -= 1
    while j >= aj_0:
        if matrix[i][j] == 0:
            matrix[i][j] = x
        x += 1
        j -= 1
    else:
        j = aj_0
        aj_0 += 1
        i -= 1
    while i >= ai_0:
        if matrix[i][j] == 0:
            matrix[i][j] = x
        x += 1
        i -= 1
    else:
        i = ai_0
        ai_0 += 1
        j = aj_0
for row in range(n):
    for col in range(m):
        print(str(matrix[row][col]).ljust(3), end='')
    print()

# Задача 4_7.1
"""
Напишите программу для вычисления суммы двух матриц.
На вход программе подаются два натуральных числа n и m — количество строк и столбцов 
в матрицах, затем элементы первой матрицы, затем пустая строка, далее следуют элементы второй матрицы.
2 4
1 2 3 4
5 6 7 1

3 2 1 2
1 3 1 3
--->>>
4 4 4 6
6 9 8 4
"""
n, m = map(int, input().split())
m1 = [[int(i) for i in input().split()] for _ in range(n)]
input()
m2 = [[int(i) for i in input().split()] for _ in range(n)]
for row in range(n):
    for col in range(m):
        x = m1[row][col] + m2[row][col]
        print(x, end=' ')
    print()
# Задача 4_7.2
"""
Напишите программу, которая перемножает две матрицы.
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы, 
На вход программе подаются два натуральных числа n и m — количество строк и столбцов в первой матрице, затем элементы 
первой матрицы, затем пустая строка. Далее следуют числа m и k — количество строк и столбцов второй матрицы затем 
элементы второй матрицы.
2 2
1 2
3 2

2 2
3 2
1 1
--->>>
5 4
11 8
"""
n, m = map(int, input().split())
m1 = [[int(i) for i in input().split()] * m for _ in range(n)]
input()
m, k = map(int, input().split())
m2 = [[int(i) for i in input().split()] * m for _ in range(m)]
m3 = [[0] * k for i in range(n)]
for i in range(n):
    for j in range(k):
        for r in range(m):
            m3[i][j] += m1[i][r] * m2[r][j]
for row in m3:
    print(*row)
    
# Задача 4_7.3
"""
Напишите программу, которая возводит квадратную матрицу в m-ую степень.
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы, 
затем натуральное число m.
3
1 2 3
4 5 6
7 8 9
2
--->>>
30 36 42
66 81 96
102 126 150
"""
n = int(input())
mat = [[int(i) for i in input().split()] for _ in range(n)]
m = int(input())
mat2 = mat.copy()
for _ in range(m-1):
    mat3 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for r in range(n):
                mat3[i][j] += mat2[i][r] * mat[r][j]
    mat2 = mat3.copy()
for row in mat2:
    print(*row)

