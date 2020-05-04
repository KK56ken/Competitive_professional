n = int(input())

a = []
s = [0] * n
a.append(input().split())

for i in range(n - 1):
    a[0][i] = int(a[0][i])
    s[a[0][i]-1] += 1

for i in range(n):
    print(s[i])
