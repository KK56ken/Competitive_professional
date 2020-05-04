n, m = map(int, input().split())

a = [[0] * 2 for i in range(n)]
h = []
check = []
cnt = 0
h = input().split()

for i in range(n):
    h[i] = int(h[i])
print(h)
for i in range(n):
    for j in range(2):
        a[i][j] = i+1
        if j == 1:
            a[i][j] = h[i]

for i in range(m):
    b, c = map(int, input().split())
    print("aのb", a[b - 1][1], "aのc", a[c - 1][1])
    if not a[b-1][1] in check or not a[c-1][1] in check:
        if a[b-1][1] > a[c-1][1]:
            check.append(a[b - 1][1])
        else:
            check.append(a[c-1][1])

print(cnt)
