'''
На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n, заполнив ее в соответствии с образцом.

Формат входных данных
На вход программе подается натуральное число n – количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом: разместить единицы на главной и побочной диагоналях,
остальные позиции матрицы заполнить нулями.

Примечание. Для вывода элементов матрицы как в примерах отводите ровно 3 символа на каждый элемент.
Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение. 😇

Тестовые данные

Sample Input 1:
5

Sample Output 1:
1  0  0  0  1
0  1  0  1  0
0  0  1  0  0
0  1  0  1  0
1  0  0  0  1
'''

#My code
n = int(input())
matrix = [[0] * n for i in range(n)]
for i in range(n):
    matrix[i][i] = 1
    matrix[i][n - i - 1] = 1

for i in range(n):
    for j in range(n):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()

#Best code 1
n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j or i + j + 1 == n:
            matrix[i][j] = 1

for row in matrix:
    print(*row)

#Best code 2
n = int(input())

res = [[1 if i == j or i == n - j - 1 else 0 for j in range(n)] for i in range(n)]

for x in res:
    print(*x)

#Best code 3
n = int(input())
for i in range(n):
    print(*[str(int(j == i or i == n - j - 1)).ljust(3)  for j in range(n)])