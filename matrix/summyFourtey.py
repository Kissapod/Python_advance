'''
Формат входных данных
На вход программе подается натуральное число n – количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Элементы диагоналей не учитываются.

Тестовые данные

Sample Input 1:
4
1 2 3 4
5 6 7 8
3 4 5 6
1 2 3 4

Sample Output 1:
Верхняя четверть: 5
Правая четверть: 14
Нижняя четверть: 5
Левая четверть: 8
'''

#My code
n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
maximum = matrix[0][0]
lst = [0] * 4

for i in range(n):
    for j in range(n):
        if i < j and i < n - 1 - j:
            lst[0] += matrix[i][j]
        elif i < j and i > n - 1 - j:
            lst[1] += matrix[i][j]
        elif i > j and i > n - 1 - j:
            lst[2] += matrix[i][j]
        elif i > j and i < n - 1 - j:
            lst[3] += matrix[i][j]

print("Верхняя четверть:", lst[0])
print("Правая четверть:", lst[1])
print("Нижняя четверть:", lst[2])
print("Левая четверть:", lst[3])

#Best code
n = int(input())
matrix = []
quadrants = [['Верхняя четверть:', 0],
             ['Правая четверть:', 0],
             ['Нижняя четверть:', 0],
             ['Левая четверть:', 0]]

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

for i in range(n):
    for j in range(n):
        if i < j and i + j + 1 < n :
            quadrants[0][1] += matrix[i][j]
        elif i < j and i + j + 1 > n:
            quadrants[1][1] += matrix[i][j]
        elif i > j and i + j + 1 > n:
            quadrants[2][1] += matrix[i][j]
        elif i > j and i + j + 1 < n:
            quadrants[3][1] += matrix[i][j]

for i in range(4):
    print(quadrants[i][0], quadrants[i][1])