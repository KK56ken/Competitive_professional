n, m = map(int, input().split())
a = 0
for i in range(m):
    a = n * m-i/n-1*m-1 + a
print(a+1)
