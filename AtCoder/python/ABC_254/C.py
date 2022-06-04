N,K = map(int,input().split())

a = list(map(int,input().split()))

l = [[] for _ in range(K)]

for i in range(N):
    l[i % K].append(a[i])
for i in range(K):
    l[i] = sorted(l[i])

a = sorted(a)

for i in range(K):
    if a[i::K] != l[i]:
        print("No")
        exit()
    
print("Yes")