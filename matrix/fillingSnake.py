'''
Sample Input 1:
3 5

Sample Output 1:
1  2  3  4  5
10 9  8  7  6
11 12 13 14 15
'''

#My code
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if (i + 1) % 2 == 0:
            matrix[i][j] = (i + 1) * m - j
        else:
            matrix[i][j] = i * m + j + 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()


#Best code
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = i * m + j + 1
    if i % 2:
        matrix[i].reverse()

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()