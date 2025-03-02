'''
На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n и заполняет ее по следующему правилу:
числа на побочной диагонали равны 1;
числа, стоящие выше этой диагонали, равны 0;
числа, стоящие ниже этой диагонали, равны 2.
Полученную матрицу выведите на экран. Числа в строке разделяйте одним пробелом.

Формат входных данных
На вход программе подается натуральное число n – количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии с условием задачи.

Примечание. Побочная диагональ – это диагональ, идущая из правого верхнего в левый нижний угол матрицы.

Тестовые данные

Sample Input 1:
4

Sample Output 1:
0 0 0 1
0 0 1 2
0 1 2 2
1 2 2 2
'''

#My code
n = int(input())
matrix = [[0] * n for _ in range(n)]
for i in range(n):
    matrix[i][n-i-1] = 1
    for j in range(n):
        if i + j >= n:
            matrix[i][j] = 2
    print(*matrix[i])

#Best code
n = int(input())
matrix = [[None for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i + j + 1 == n:
            matrix[i][j] = 1
        elif i + j + 1 < n:
            matrix[i][j] = 0
        else:
            matrix[i][j] = 2

for row in matrix:
    print(*row)

#--------

n = int(input())
q = [[(i >= n - j - 1) + (i > n - j - 1) for j in range(n)] for i in range(n)]
for e in q:
    print(*e)