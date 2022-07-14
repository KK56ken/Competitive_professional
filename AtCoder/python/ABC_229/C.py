n,w = map(int,input().split())
l = [[0] for _ in range(n)]
# l = [[]]

for i in range(n):
    a,b = map(int,input().split())
    l[i][0] = a
    l[i].append(b)
    
l = sorted(l, reverse=True, key=lambda x: x[0])  
suma = 0

g = 0
# print(l)
for i in range(n):
    g = l[i][1]
    if w >= g:
        suma += l[i][0] * l[i][1]
    else:
        g -= l[i][1]
        suma += (w-g) * l[i][0]
    # print(suma)
print(suma)