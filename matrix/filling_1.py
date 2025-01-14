'''
На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m
и заполняет ее числами от 1 до n в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа n и m – количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии с образцом.

Примечание. Для вывода элементов матрицы как в примерах отводите ровно 3 символа на каждый элемент.
Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение.

Тестовые данные

Sample Input 1:
3 4

Sample Output 1:
1  2  3  4
5  6  7  8
9  10 11 12
'''

#My code
n, m = [int(i) for i in input().split()]
count = 1
matrix = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        matrix[i][j] = count
        count += 1
        print(str(matrix[i][j]).ljust(2), end=' ')
    print()

#Best code
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = i * m + j + 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()

#------------

n, m = [int(i) for i in input().split()]
matrix = [list(range(m*i + 1, m*i + 1 + m)) for i in range(n)]

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()