n = int(input())

S = {}
result = []
for i in range(n):
    qs = list(map(int,input().split(" ")))
    if qs[0] == 1:
        try:
            S[qs[1]] = S[qs[1]] + 1
        except KeyError:
            S[qs[1]] = 1
    elif qs[0] == 2:
        try:
            S[qs[1]] = S[qs[1]] - min(qs[2],S[qs[1]])
        except KeyError:
            continue
        if S[qs[1]] == 0:
            S.pop(qs[1])        
    elif qs[0] == 3:
        result.append(max(S) - min(S)) 

for i in range(len(result)):
    print(result[i])
