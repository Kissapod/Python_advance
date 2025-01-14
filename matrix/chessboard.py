'''
На вход программе подаются два натуральных числа n и m. Напишите программу для создания матрицы размером n × m?
заполнив ее символами . и * в шахматном порядке.
В левом верхнем углу должна стоять точка. Выведите полученную матрицу на экран, разделяя элементы пробелами.

Формат входных данных
На вход программе на одной строке через пробел подаются два натуральных числа n и m – количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу, описанную в условии задачи.

Тестовые данные

Sample Input 1:
3 4

Sample Output 1:
. * . *
* . * .
. * . *
'''

#My code
s = input().split()
n, m = int(s[0]), int(s[1])
matrix = [
    ["." for _ in range(m)]
    for _ in range(n)
]
for i in range(n):
    for j in range(m):
        if (i + j) % 2 != 0:
            matrix[i][j] = "*"
    print(*matrix[i])

#Best code
n, m = [int(i) for i in input().split()]
board = [['.'] * m for _ in range(n)]

for i in range(n):
    for j in range(1 - i % 2, m, 2):
        board[i][j] = '*'

for row in board:
    print(*row)

#--------

n, m = map(int, input().split())
for i in range(n):
    row = ['.' if (i + j) % 2 == 0 else '*' for j in range(m)]
    print(*row)