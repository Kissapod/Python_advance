"""
 На вход программе подается число n. Напишите программу, которая создает и выводит построчно список,
    состоящий из n списков [[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].

Формат входных данных
    На вход программе подается натуральное число n.

Формат выходных данных
    Программа должна вывести построчно указанный список.

Тестовые данные 🟢

Sample Input 1:
    3
 Sample Output 1:
    [1, 2, 3]
    [1, 2, 3]
    [1, 2, 3]
"""

#My code
n = int(input())

for _ in range(n):
    new_lst = []
    for i in range(n):
        new_lst.append(i+1)
    print(new_lst)

#Best code
n = int(input())
result = []

for _ in range(n):
    result.append(list(range(1, n + 1)))

print(*result, sep='\n')