'''
Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке, больших среднего арифметического элементов данной строки.

Формат входных данных
На вход программе подается натуральное число n – количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести n чисел – для каждой строки количество элементов матрицы, больших среднего арифметического элементов данной строки.

Тестовые данные

Sample Input 1:
4
1 2 3 4
5 6 3 15
0 2 3 1
5 2 8 5

Sample Output 1:
2
1
2
1
'''

#My code
n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    count = 0
    meanArith = sum(matrix[i]) / len(matrix[i])
    for j in range(n):
        if matrix[i][j] > meanArith:
            count += 1
    print(count)

#Best code
n = int(input())
matrix = []

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

for i in range(n):
    counter = 0
    average = sum(matrix[i]) / n
    for j in range(n):
        if matrix[i][j] > average:
            counter += 1
    print(counter)