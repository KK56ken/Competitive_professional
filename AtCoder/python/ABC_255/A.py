R,C = map(int,input().split())

a1,a2 = map(int,input().split())
a3,a4 = map(int,input().split())

if R == 1 and C == 1:
    print(a1)
elif R == 1 and C == 2:
    print(a2)
elif R == 2 and C == 1:
    print(a3)
elif R == 2 and C == 2:
    print(a4)

