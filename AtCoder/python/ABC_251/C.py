def juge(tmp, S, index, second, N):
    cnt = 0
    print("second",second%10)
    while(True):
        if index >= N-1:
            break
        if tmp == int(S[index][second % 10]):
            return juge(tmp,S,index+1,second,N)
        second += 1
        cnt += 1
        if cnt >= 10:
            break
    return second

N = int(input())

S = []
a = []

for i in range(N):
    S.append(input())
for i in range(10):
    second = 1
    tmp = int(S[0][i])
    a.append(juge(tmp, S, 1, second,N))

print(min(a))