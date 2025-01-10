'''
Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.

Формат входных данных
На вход программе подается натуральное число n – количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.

Формат выходных данных
Программа должна вывести YES, если матрица симметрична относительно главной диагонали, или NO в противном случае.

Тестовые данные

Sample Input 1:
3
0 1 2
1 2 3
2 3 4

Sample Output 1:
YES
'''

#My code
n = int(input())
matrix = [input().split() for _ in range(n)]
flag = True
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if matrix[i][j] != matrix[j][i]:
            flag = False
            break
    if not flag:
        break
if flag:
    print("YES")
else:
    print("NO")


#Best code
n = int(input())
matrix = [input().split() for _ in range(n)]
result = 'YES'

for i in range(n):
    for j in range(i + 1, n):
        if matrix[i][j] != matrix[j][i]:
            result = 'NO'
            break
    if result == 'NO':
        break

print(result)