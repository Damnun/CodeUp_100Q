target = int(input())
tmp = 0
count = 1
while True:
    tmp += count
    count += 1
    if tmp >= target:
        print(tmp)
        break