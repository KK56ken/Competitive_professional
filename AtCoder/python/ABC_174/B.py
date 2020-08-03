import math

cnt = 0 
n, d = map(int, input().split())

for i in range(n):
    x, y = map(int, input().split())
    a = math.sqrt(x ** 2 + y ** 2)
    if d >= a:
        cnt += 1

print(cnt)