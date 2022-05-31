h,w = map(int,input().split())

l = []
y = []
x = []

for i in range(h):
    l.append(input())

for i in range(h):
    for j in range(w):
        if l[i][j] == "o":
            y.append(i)
            x.append(j)
print(abs(x[0]-x[1])+abs(y[0]-y[1]))
