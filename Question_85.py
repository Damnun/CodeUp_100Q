w, h, b = map(int, input().split())
result = (w * h * b) / 1024 / 8
result /= 1024
print("%.2f" %result + " MB")