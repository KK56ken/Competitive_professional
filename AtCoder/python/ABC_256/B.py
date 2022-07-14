n = int(input())

A = list(map(int,input().split()))
masu = [0,0,0,0]
p = 0
for i in A:
    masu[0] = 1
    if i == 1:
        for j in reversed(range(len(masu))):
            if masu[j] and j == 3:
                masu[j] = 0
                p += 1
            elif masu[j]:
                masu[j] = 0
                masu[j+1] = 1
        
    if i == 2:
        for j in reversed(range(len(masu))):
            if masu[j] and j == 3 or masu[j] and j == 2:
                masu[j] = 0
                p += 1
            elif masu[j]:
                masu[j] = 0
                masu[j+2] = 1
                
    if i == 3:
        for j in reversed(range(len(masu))):
            if masu[j] and j == 3 or masu[j] and j == 2 or masu[j] and j == 1:
                masu[j] = 0
                p += 1
            elif masu[j]:
                masu[j] = 0
                masu[j+3] = 1
                
    if i == 4:
        p += masu[0]+masu[1]+masu[2]+masu[3]
        masu[0] = 0
        masu[1] = 0
        masu[2] = 0
        masu[3] = 0

print(p)