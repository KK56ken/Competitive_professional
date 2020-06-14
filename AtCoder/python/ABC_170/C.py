
p = []
cnt = 0
x, n = map(int, input().split())

p = input().split()

for i in range(n):
    p[i] = int(p[i])

while True:
    if not x in p:
        print(x)
        break
    if cnt % 2 == 0:
        x = x - (cnt + 1)
    elif cnt % 2 == 1:
        x = x + (cnt + 1)
    cnt += 1
