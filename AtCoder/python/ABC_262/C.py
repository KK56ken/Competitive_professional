def judge(a,b,l):
    if [a,b] in l:
        return 1
    else:
        return 0

n,m = map(int,input().split())

l = []
dst = {}
for i in range(m):
    l.append(list(map(int,input().split())))

l = sorted(l)
