import itertools

def judge(a,b,l):
    if [a,b] in l:
        return 1
    else:
        return 0

n,m = map(int,input().split())

l = []

for i in range(m):
    l.append(list(map(int,input().split())))

l = sorted(l)

a = []
cnt = 0
result = 0

# print()

for i in range(1,m):
    if l[i-1][0] == l[i][0]:
        a.append(l[i-1+cnt][1])
        a.append(l[i+cnt][1])
        # cnt += 1
    else:
        a = list(set(a))
        for pair in itertools.combinations(a, 2):
            result += judge(pair[0],pair[1],l)
            # print(pair)
        a = []
print(result)

