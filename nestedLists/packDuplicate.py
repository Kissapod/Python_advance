'''
Упаковка дубликатов 🌶️
На вход программе подается строка текста, содержащая символы. Напишите программу,
которая упаковывает последовательности одинаковых символов заданной строки в подсписки.

Формат входных данных
На вход программе подается строка текста, содержащая символы, разделенные символом пробела.

Формат выходных данных
Программа должна вывести указанный вложенный список.

Тестовые данные

Sample Input 1:
a b c d
Sample Output 1:
[['a'], ['b'], ['c'], ['d']]

Sample Input 2:
w w w o r l d g g g g r e a t t e c c h e m g g p w w
Sample Output 2:
[['w', 'w', 'w'], ['o'], ['r'], ['l'], ['d'], ['g', 'g', 'g', 'g'], ['r'], ['e'], ['a'], ['t', 't'], ['e'], ['c', 'c'], ['h'], ['e'], ['m'], ['g', 'g'], ['p'], ['w', 'w']]
'''

#My code
lst = []
lastChar = ""
lastLst = []

s = input().split(" ")

for c in s:
    if c != lastChar:
        lastChar = c
        newLst = list()
        lastLst = newLst
        lst.append(lastLst)
    lastLst.append(c)

print(lst)

#Best code
s = input().split()
# кидаем первый символ в наш список, также удалив его из входного списка
seq = [[s.pop(0)]]

for c in s:
    if c in seq[-1]:
        seq[-1].append(c)
    else:
        seq.append([c])

print(seq)