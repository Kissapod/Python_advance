'''
Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов, имеющая треугольную форму. В этом треугольнике на вершине и по бокам стоят единицы. Каждое число равно сумме двух расположенных над ним чисел.

0:      1
1:     1 1
2:    1 2 1
3:   1 3 3 1
4:  1 4 6 4 1
      .....
На вход программе подается число n. Напишите программу, которая возвращает указанную строку треугольника Паскаля
в виде списка (нумерация строк начинается с нуля).

Формат входных данных
На вход программе подается число n (n≥0).

Формат выходных данных
Программа должна вывести указанную строку треугольника Паскаля в виде списка.

Sample Input 3:
2

Sample Output 3:
[1, 2, 1]

Sample Input 4:
3

Sample Output 4:
[1, 3, 3, 1]
'''

#My code
def factorial(n):
    k = 1
    f = 1
    while k <= n:
        f *= k
        k += 1
    return f

def pascal(strokeNumber):
    lst = [0] * (strokeNumber + 1)
    for i in range(len(lst)):
        res = factorial(strokeNumber) / (factorial(i) * factorial(strokeNumber - i))
        lst[i] = int(res)
    return lst

n = int(input())

print(pascal(n))

#Best code
def pascal(n):
    # начальная строка
    cur_seq = [1]

    for _ in range(n):
        # добавляем нули по бокам к текущей строке строке
        cur_seq = [0] + cur_seq + [0]
        # тут будет храниться новая строка
        new_seq = []

        for i in range(len(cur_seq) - 1):
            # добавляем в новую строку сумму соседних элементов текущей строки
            new_seq.append(cur_seq[i] + cur_seq[i + 1])

        # теперь новая строка становится нашей текущей строкой
        cur_seq = new_seq

    return cur_seq


n = int(input())
print(pascal(n))