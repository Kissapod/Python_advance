'''
Напишите программу, которая поворачивает квадратную матрицу чисел на 90∘ по часовой стрелке.

Формат входных данных
На вход программе подается натуральное число n – количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.

Формат выходных данных
Программа должна вывести результат на экран, числа должны быть разделены одним пробелом.

Тестовые данные

Sample Input 1:
3
1 2 3
4 5 6
7 8 9

Sample Output 1:
7 4 1
8 5 2
9 6 3
'''

#My code
n = int(input())
matrix = [input().split() for _ in range(n)]
newList = []
for i in range(n):
    seq = []
    for j in range(n):
        val = matrix[n-j-1][i]
        seq.append(val)
    newList.append(seq)
for raw in newList:
    print(*raw)

#Best code
n = int(input())
matrix = [input().split() for _ in range(n)]
result = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        result[i][j] = matrix[n - j - 1][i]

for row in result:
    print(*row)