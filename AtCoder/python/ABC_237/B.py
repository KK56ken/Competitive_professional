h,w = map(int,input().split())
a = []

for i in range(h):
    a.append(list(map(int,input().split())))

for i in range(w):
    for j in range(h):
        print(a[j][i],end=" ")
    print()

# for i in range(h):
#     for j in range(w):
#         print(a[i][j],end="")