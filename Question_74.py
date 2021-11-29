target = ord(input())
n = 'a'

while ord(n) != target + 1:
    print(n, end=' ')
    n = chr(ord(n) + 1)