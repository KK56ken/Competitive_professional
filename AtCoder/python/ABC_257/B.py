n,k,q = map(int,input().split())

a = list(map(int,input().split()))

l = list(map(int,input().split()))

for i in range(len(l)):
    if a[l[i]-1] != n:
        if k == l[i]:
            a[l[i]-1] += 1
        else:
            if a[l[i]] != a[l[i]-1] + 1:
                a[l[i]-1] += 1
for i in range(len(a)):
    print(a[i],end=" ")
print()