'''
Sample Input 1:
4 5

Sample Output 1:
1  2  3  4  5
14 15 16 17 6
13 20 19 18 7
12 11 10 9  8
'''

#My code
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]
i, j = 0, 0
currentDirection = "right"
for q in range(1, n * m + 1):
    matrix[i][j] = q
    if currentDirection == "right":
        j += 1
        if j >= m or matrix[i][j] != 0:
            currentDirection = "down"
            j -= 1
            i += 1
    elif currentDirection == "down":
        i += 1
        if i >= n or matrix[i][j] != 0:
            currentDirection = "left"
            i -= 1
            j -= 1
    elif currentDirection == "left":
        j -= 1
        if j < 0 or matrix[i][j] != 0:
            currentDirection = "up"
            j += 1
            i -= 1
    elif currentDirection == "up":
        i -= 1
        if i < 0 or matrix[i][j] != 0:
            currentDirection = "right"
            i += 1
            j += 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()

#Best code 1
n, m = [int(i) for i in input().split()]

matrix = [[0] * m for _ in range(n)]
counter = 1
rows_passed, columns_passed = 0, 0
current_row, current_column = 0, 0

for k in range(n * m):
    if counter == n * m + 1:
        break
    direction = k % 4
    if direction == 0:
        for j in range(columns_passed, m - columns_passed):
            matrix[current_row][j] = counter
            counter += 1
        current_column = j
        rows_passed += 1
    elif direction == 1:
        for i in range(rows_passed, n - rows_passed + 1):
            matrix[i][current_column] = counter
            counter += 1
        current_row = i
        columns_passed += 1
    elif direction == 2:
        for j in range(current_column - 1, columns_passed - 2, -1):
            matrix[current_row][j] = counter
            counter += 1
        current_column = j
    elif direction == 3:
        for i in range(current_row - 1, rows_passed - 1, -1):
            matrix[i][current_column] = counter
            counter += 1
        current_row = i

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()

#Best code 2
n, m = [int(num) for num in input().split()]

i = 0
j = 0
cnt = 1

a = [[0 for _ in range(m)] for _ in range(n)]

while cnt < m * n:
    while j < m - 1 and a[i][j + 1] == 0:
        a[i][j] = cnt
        j += 1
        cnt += 1

    while i < n - 1 and a[i + 1][j] == 0:
        a[i][j] = cnt
        i += 1
        cnt += 1

    while j > 0 and a[i][j - 1] == 0:
        a[i][j] = cnt
        j -= 1
        cnt += 1

    while i > 0 and a[i - 1][j] == 0:
        a[i][j] = cnt
        i -= 1
        cnt += 1

a[i][j] = cnt

for i in range(n):
    for j in range(m):
        print(str(a[i][j]).ljust(3), end=' ')
    print()

#Best code 3
n, m = map(int, input().split())
a = [[0] * m for _ in range(n)]
dr, dc, r, c = 0, 1, 0, 0

for cnt in range(1, n * m + 1):
    a[r][c] = cnt

    if a[(r + dr) % n][(c + dc) % m]:
        dr, dc = dc, -dr

    r += dr
    c += dc

for row in a:
    print(*(f'{e:<3}' for e in row), sep='')