S = list(input())
a,b = map(int,input().split())
a = a - 1
b = b - 1

tmp = S[a]
S[a] = S[b]
S[b] = tmp

for i in range(len(S)):
    print(S[i],end="")
print()
