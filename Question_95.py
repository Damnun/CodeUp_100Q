matrix = [[0 for _ in range(19)] for _ in range(19)]
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    matrix[x - 1][y - 1] = 1

for i in matrix:
    for j in i:
        print(j, end=' ')
    print()
