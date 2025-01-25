'''
Sample Input 1:
3 5

Sample Output 1:
1  2  4  7  10
3  5  8  11 13
6  9  12 14 15
'''

#My code
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]
nm = 0
for q in range(n * m):
    for i in range(n):
        for j in range(m):
            if i + j == q:
                nm += 1
                matrix[i][j] = nm

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()


#Best code 1
n, m = [int(el) for el in input().split()]
matrix = [[None for _ in range(m)] for _ in range(n)]
cnt = 1

# проходим по всем диагоналям
for d in range(n + m - 1):
    for i in range(n):
        for j in range(m):
            if i + j == d:
                matrix[i][j] = cnt
                cnt += 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end="")
    print()

#Best code 2
n, m = [int(i) for i in input().split()]

matrix = [[1] * m for _ in range(n)]
row, col, diag = 0, 0, 0

for i in range(1, n * m):
    col -= 1
    row += 1
    if col < 0 or row == n:
        diag += 1
        col = diag if diag < m else m - 1
        row = diag - col

    matrix[row][col] += i

[print(*i) for i in matrix]