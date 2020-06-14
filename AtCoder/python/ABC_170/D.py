a = []
cnt = 0

n = int(input())
a = list(map(int, input().split()))
a = sorted(a)

for i in range(n):
    for j in range(n):
        if not i == j and a[i] % a[j] == 0:
            cnt += 1
            break

print(n-cnt)
