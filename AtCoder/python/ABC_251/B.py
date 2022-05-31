N,K = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

result = []

for i,v in enumerate(A):
    if v == max(A):
        result.append(i+1)


for v in result:
    if v in B:
        print("Yes")
        exit()
print("No")