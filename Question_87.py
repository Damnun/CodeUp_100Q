target = int(input())

for i in range(target + 1):
    if i % 3 == 0:
        continue
    print(i)
