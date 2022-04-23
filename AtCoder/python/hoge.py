N = int(input())
A = list(map(int, input().split()))
Q = int(input())
query = [list(map(int, input().split())) for _ in range(Q)]

numPos = {}

for i in range(N):
    if A[i] not in numPos:
        numPos[A[i]] = []
    numPos[A[i]].append(i + 1)

for l, r, x in query:
    if x not in numPos:
        print(0)
    else:
        pass
