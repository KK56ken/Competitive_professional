n, x, t = map(int, input().split())
time = 0

while n > 0:
    n = n - x
    time += t


print(time)
