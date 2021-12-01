matrix = []
for _ in range(19):
    matrix.append(list(map(int, input().split())))

count = int(input())
for i in range(count):
    x, y = map(int, input().split())
    for j in range(19):
        if matrix[x - 1][j] == 0:
            matrix[x - 1][j] = 1
        else:
            matrix[x - 1][j] = 0
    for j in range(19):
        if matrix[j][y - 1] == 0:
            matrix[j][y - 1] = 1
        else:
            matrix[j][y - 1] = 0

for i in matrix:
    for j in i:
        print(j, end=' ')
    print()