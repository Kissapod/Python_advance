'''
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

и и и дуде
швец жнец на игрец
'''

#My code
n, m = int(input()), int(input())
matrix = [[input() for _ in range(m)] for _ in range(n)]

for row in matrix:
    print(*row)

print()

for r in range(m):
    for c in range(n):
        print(matrix[c][r], end=' ')
    print()

#Best code