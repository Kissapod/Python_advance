'''
Магическим квадратом порядка n называется квадратная таблица размера n×n, составленная из всех чисел 1,2,3, …, n^2 так,
что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой. Напишите программу,
которая проверяет, является ли заданная квадратная матрица магическим квадратом.

Формат входных данных
На вход программе подается натуральное число n – количество строк и столбцов в матрице, затем элементы матрицы:
n строк, по n чисел в каждой, разделенные пробелами.

Формат выходных данных
Программа должна вывести YES, если матрица является магическим квадратом, или NO в противном случае.

Тестовые данные

Sample Input 1:
3
8 1 6
3 5 7
4 9 2

Sample Output 1:
YES
'''

#My code
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

lst = [int(i) for i in range(1, n * n + 1)]
flag = "YES"
totalRaw = sum(matrix[0])
totalMain = 0
totalSubMain = 0

for i in range(n):
    totalCol = 0
    totalMain += matrix[i][i]
    totalSubMain += matrix[i][n - i - 1]
    for j in range(n):
        totalCol += matrix[j][i]
        if matrix[i][j] not in lst:
            flag = "NO"
            break
        lst.pop(lst.index(matrix[i][j]))
    if totalCol != totalRaw or sum(matrix[i]) != totalRaw:
        flag = "NO"
        break
if totalMain != totalSubMain != totalRaw:
    flag = "NO"

print(flag)

#Best code
def is_magic_square(n, matrix):
    # создаем список для всех чисел правильной матрицы
    correct_nums = list(range(1, n ** 2 + 1))

    # создаем список для всех чисел нашей матрицы
    our_nums = []
    for row in matrix:
        our_nums.extend(row)

    # если эти списки не равны, значит наша матрица уже не состоит из всех чисел от 1 до n ** 2
    # значит, мы сразу можем вернуть "NO" и не продолжать дальнейшие проверки
    our_nums.sort()
    if our_nums != correct_nums:
        return "NO"

    # в самой матрице мы уже храним все ряды (строки)
    rows = matrix.copy()

    # создаем список для всех столбцов
    columns = []
    for j in range(n):
        cur_column = []
        for i in range(n):
            cur_column.append(matrix[i][j])

        columns.append(cur_column)

    # создаем список для диагоналей (с двумя пустыми подсписками)
    diagonals = [[], []]
    for i in range(n):
        diagonals[0].append(matrix[i][i])
        diagonals[1].append(matrix[i][n - 1 - i])

    # соединям все строки, столбцы и диагонали в один список
    all_lines = rows + columns + diagonals

    # инициализируем переменные для максимальной и минимальной суммы среди всех "линий"
    # за начальные значения возьмём сумму первой "линии"
    max_sum = sum(all_lines[0])
    min_sum = sum(all_lines[0])
    for line in all_lines:
        max_sum = max(max_sum, sum(line))
        min_sum = min(min_sum, sum(line))

    # теперь просто сравниваем максимальную и минимальную суммы
    # они должны быть равны, т.к. все суммы должны быть равны
    if max_sum != min_sum:
        return "NO"

    return "YES"

n = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(n)]

print(is_magic_square(n, matrix))