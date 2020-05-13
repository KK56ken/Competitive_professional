n, m = map(int, input().split())
suma = 0
a = []
a.append(input().split())

for i in range(m):
    a[0][i] = int(a[0][i])
for i in range(m):
    suma = a[0][i] + suma

if n < suma:
    print(-1)
else:
    print(n-suma)
