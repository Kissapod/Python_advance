'''Разбиение на чанки 🌶️
На вход программе подаются две строки: на одной – символы, на другой – число n. Из первой строки формируется список.

Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка (куска), а возвращает список из чанков (кусков) указанной длины.

Формат входных данных
На вход программе подаются строка текста, содержащая символы, разделенные символом пробела, и число n на отдельной строке.

Формат выходных данных
Программа должна вывести указанный вложенный список.

Примечание. Не забудьте вызвать функцию chunked(), чтобы вывести результат. 😀

Тестовые данные
Sample Input 1:
a b c d e f
2
Sample Output 1:
[['a', 'b'], ['c', 'd'], ['e', 'f']]

Sample Input 2:
a b c d e f
3
Sample Output 2:
[['a', 'b', 'c'], ['d', 'e', 'f']]
'''

#My code
def chunked(lst, n):
    newLst = []
    seq = [lst[0]]
    for i in range(1, len(lst)):
        if i%n == 0:
            newLst.append(seq)
            seq = list(lst[i])
        else:
            seq.append(lst[i])
    newLst.append(seq)
    return newLst
s = input().split(" ")
n = int(input())

print(chunked(s, n))

#Best code
def chunked(symbols, n):
    result = []
    for i in range(0, len(symbols), n):
        result.append(symbols[i:i + n])
    return result

symbols = input().split()
n = int(input())

print(chunked(symbols, n))