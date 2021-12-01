h, w = map(int, input().split())
n = int(input())
matrix = [[0 for _ in range(w)] for _ in range(h)]

"""
d = 0 // 가로
d = 1 // 세로
"""
for i in range(n):
    l, d, x, y = map(int, input().split())
    x -= 1
    y -= 1

    for j in range(l):
        matrix[x][y] = 1
        if d == 0:
            y += 1
        else:
            x += 1

for i in matrix:
    for j in i:
        print(j, end=' ')
    print()