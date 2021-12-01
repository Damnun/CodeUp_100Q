data = [0 for _ in range(24)]
count = int(input())
target = list(map(int, input().split()))

for i in target:
    data[i] += 1
for i in range(1, 24):
    print(data[i], end=' ')