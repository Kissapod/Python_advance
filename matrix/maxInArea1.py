'''
Формат входных данных
На вход программе подается натуральное число n – количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.

1 0 0
1 1 0
1 1 1

Формат выходных данных
Программа должна вывести одно число – максимальный элемент в заштрихованной области квадратной матрицы.

Примечание. Элементы главной диагонали также учитываются.

Тестовые данные

Sample Input 1:
3
1 4 5
6 7 8
1 1 6

Sample Output 1:
7
'''

#My code
n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
maximum = matrix[0][0]
for i in range(n):
    for j in range(i+1):
        if matrix[i][j] > maximum:
            maximum = matrix[i][j]
print(maximum)

#Best code
n = int(input())
matrix = []

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

largest = matrix[0][0]

for i in range(n):
    for j in range(n):
        if i >= j and matrix[i][j] > largest:
            largest = matrix[i][j]

print(largest)