n,q = map(int,input().split())

a = list(map(int,input().split()))
d = {}
result = []
i = 1
for v in a:
    d[v] = []

for v in a:
    d[v].append(i)
    i += 1

for i in range(q):
    x,k = map(int,input().split())
    
    try:
        result.append(d[x][k-1])
    except KeyError:
        result.append(-1)
    except IndexError:
        result.append(-1)

for v in result:
    print(v)