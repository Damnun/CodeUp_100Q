"""
1초/ 소리강약 체크 횟수 /h
체크 값 저장 비트 수 / b
트랙 채널개수 /c
시간 /s

"""

h, b, c, s = map(int, input().split())
result = (h * b * c * s) / 8
result /= 1024**2
print("%.1f" %result +" MB")