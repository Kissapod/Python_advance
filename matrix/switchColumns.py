'''
Напишите программу, которая меняет местами столбцы в матрице.

Формат входных данных
На вход программе на разных строках подаются два натуральных числа n и m – количество строк и столбцов в матрице,
затем элементы матрицы построчно через пробел, затем натуральные числа i и j – номера столбцов, подлежащих обмену.

Формат выходных данных
Программа должна вывести указанную таблицу с замененными столбцами.

Тестовые данные

Sample Input 1:
3
4
11 12 13 14
21 22 23 24
31 32 33 34
0 1

Sample Output 1:
12 11 13 14
22 21 23 24
32 31 33 34
'''

#My code
n, m = int(input()), int(input())
matrix = [[i for i in input().split()] for _ in range(n)]
switch = [int(i) for i in input().split()]
for i in range(n):
    matrix[i][switch[0]], matrix[i][switch[1]] = matrix[i][switch[1]], matrix[i][switch[0]]
    print(*matrix[i])

#Best code
n, m = int(input()), int(input())
matrix = [input().split() for _ in range(n)]
col1, col2 = [int(i) for i in input().split()]

for i in range(n):
    matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]

for row in matrix:
    print(*row)