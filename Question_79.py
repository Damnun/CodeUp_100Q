data = int(input())
sum = 0
for i in range(data + 1):
    sum += i
    if sum >= data:
        print(i)
        break