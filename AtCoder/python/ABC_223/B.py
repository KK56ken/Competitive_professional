S = list(input())

mina = 10000
maxa = 0

result = ["",""]

for i in range(len(S)):
    suma = 0
    for a in S:
        suma += int(ord(a))
    
    if maxa < suma:
        maxa = suma
        print(S)
        result[0] = "".join(S)
    
    elif mina > suma:
        mina = suma
        result[1] = "".join(S)
        
    tmp = S.pop(0)
    S.append(tmp)
    print(S)
for v in result:
    print(v)