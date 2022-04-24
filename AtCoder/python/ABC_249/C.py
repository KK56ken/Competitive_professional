import collections
import re
def main():
    N,K = map(int,input().split())
    a = []
    maxa = 0
    for i in range(N):
        a.append(input())

    for i in range(2 ** N):
        S = []
        for j in range(N):
            if ((i >> j) & 1):
                S[len(S):len(S)] = re.split('(.)', a[j])[1::2]
        c = collections.Counter(S)
        maxa = max(maxa,len([i[0] for i in c.items() if i[1] == K]))
        # maxa = len([i[0] for i in c.items() if i[1] == K])

    print(maxa)


main()