a, b, c = map(int, input().split())
target = 1
while True:
    if target % a == 0 and target % b == 0 and target % c == 0:
        break
    target += 1
print(target)