n,m = map(int,input().split())


s = input().split()
t = set(input().split())

print(s,t)
for x in s:
    if x in t:
        print("Yes")
    else:
        print("No")
    # print("Yes" if x in t else "No")