'''
На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n, заполнив ее в соответствии с образцом.

Формат входных данных
На вход программе подается натуральное число n – количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом.

Примечание. Для вывода элементов матрицы как в примерах отводите ровно 3 символа на каждый элемент.
Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение.

Тестовые данные
Sample Input 1:
5

Sample Output 1:
1  1  1  1  1
0  1  1  1  0
0  0  1  0  0
0  1  1  1  0
1  1  1  1  1
'''

#My code
n = int(input())
matrix = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if (i <= j and i <= n - j - 1) or (i >= j and i >= n - j - 1):
            matrix[i][j] = 1
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()

#Best code 1
n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if (i <= j and i + j + 1 <= n) or (i >= j and i + j + 1 >= n):
            matrix[i][j] = 1

for i in range(n):
    for j in range(n):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()

#Best code 2
n = int(input())
q = [[((i - j) * (n - i - j - 1) >= 0) * 1 for i in range(n)] for j in range(n)]
for x in q:
    print(*x, sep='  ')