
x,k,d = map(int,input().split())
mina = 1000000000000000
cnt = 0

for i in range(k):
    if abs((x + d)) > abs((x - d)):
        x = abs(x - d)
    elif abs((x - d)) > abs((x + d)):
        x = abs(x + d)
    if mina > x:
        mina = x
        cnt = 0
    else:
        cnt += 1
    if cnt >= 5:
        break

print(x)
