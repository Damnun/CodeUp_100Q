data = int(input())

for i in range(1, data + 1):
    if (i % 10) % 3 == 0 and i % 10 != 0:
        print("X", end=' ')
    else:
        print(i, end=' ')
