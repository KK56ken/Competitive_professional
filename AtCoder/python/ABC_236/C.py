n,m = map(int,input().split())


S = list(map(str,input().split(" ")))
T = set(map(str,input().split(" ")))

for a in S:
    if a in T:
        print("Yes")
    else:
        print("No")