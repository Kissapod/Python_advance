'''
На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m, заполнив ее в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа n и m – количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом.

Примечание. Для вывода элементов матрицы как в примерах отводите ровно 3 символа на каждый элемент.
Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение.

Тестовые данные
Sample Input 1:

3 7
Sample Output 1:

1  4  7  10 13 16 19
2  5  8  11 14 17 20
3  6  9  12 15 18 21
'''

#My code
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        matrix[i][j] = j * n + i + 1
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()

#Best code 1
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

for j in range(m):
    for i in range(n):
        matrix[i][j] = j * n + i + 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()

#Best code 2
n, m = [int(i) for i in input().split()]
matrix = [
    list(range(i + 1, i + 1 + n * (m - 1) + 1, n))
    for i in range(n)
]

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=" ")
    print()