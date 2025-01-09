'''
На вход программе подаются два натуральных числа n и m – количество строк и столбцов в матрице. Создайте матрицу mult
размером n×m и заполните ее таблицей умножения по формуле mult[i][j] = i * j.

Формат входных данных
На вход программе на разных строках подаются два числа n и m – количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести таблицу умножения отводя на вывод каждого числа ровно 3 символа (для этого используйте строковый метод ljust()).

Тестовые данные

Sample Input 1:
4
6

Sample Output 1:
0  0  0  0  0  0
0  1  2  3  4  5
0  2  4  6  8  10
0  3  6  9  12 15
'''

#My code
n, m = int(input()), int(input())
matrix = [[int(i) for i in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        print(i*j, end = " ")
    print()

#Best code
n, m = int(input()), int(input())
mult = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        mult[i][j] = i * j

for i in range(n):
    for j in range(m):
        print(str(mult[i][j]).ljust(3), end=' ')
    print()