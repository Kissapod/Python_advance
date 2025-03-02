'''На вход программе подаются два натуральных числа n и m,
каждое на отдельной строке – количество строк и столбцов в матрице.
Далее вводятся сами элементы матрицы – слова, каждое на отдельной строке; подряд идут элементы сначала первой строки, затем второй, и так далее.

Напишите программу, которая сначала считывает элементы матрицы один за другим, затем выводит их в виде матрицы.

Формат входных данных
На вход программе подаются два числа n и m – количество строк и столбцов в матрице, далее идут n×m слов, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести считанную матрицу, разделяя ее элементы одним пробелом.

Тестовые данные
Sample Input 1:
4
2
и
швец
и
жнец
и
на
дуде
игрец

Sample Output 1:
и швец
и жнец
и на
дуде игрец
'''

#My code
n , m = int(input()), int(input())
lst = []
for r in range(n):
    seq = []
    for c in range(m):
        seq.append(input())
    lst.append(seq)

for r in range(n):
    for c in range(m):
        print(lst[r][c], end=' ')
    print()

#Best code
n, m = int(input()), int(input())
matrix = [[input() for _ in range(m)] for _ in range(n)]

for row in matrix:
    print(*row)