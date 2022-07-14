N = int(input())
S = input()

W = list(map(int,input().split()))

mina = min(W)
maxa = max(W)

ave = sum(W) // len(W)
print(mina,maxa,ave)

micnt = 0
macnt = 0
avecnt = 0

for i in range(N):
    if mina < W[i] and S[i] == "1":
        micnt += 1
    elif mina >= W[i] and S[i] == "0":
        micnt += 1
    if maxa <= W[i] and S[i] == "1":
        macnt += 1
    elif maxa >= W[i] and S[i] == "0":
        macnt += 1
    if ave < W[i] and S[i] == "1":
        avecnt += 1
    elif ave >= W[i] and S[i] == "0":
        avecnt += 1
        
print(max(micnt,macnt,avecnt))