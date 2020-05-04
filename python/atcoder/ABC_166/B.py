n, k = map(int, input().split())
a = [0] * n
cnt = 0
b = []

for i in range(k):
    d = int(input())
    b.append(input().split())
    # print(b)

    for j in range(d):
        b[i][j] = int(b[i][j])
        a[b[i][j] - 1] += 1
for i in range(n):
    if a[i] == 0:
        cnt += 1

print(cnt)
