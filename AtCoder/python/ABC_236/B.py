import collections

n = int(input())
a = list(map(int,input().split()))


c = collections.Counter(a)

for item in c.items():
    if item[1] == 3:
        print(item[0])
        exit()

