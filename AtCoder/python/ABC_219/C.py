def main():
    X = input()
    N = int(input())
    S = []
    change = {}

    for (index, e) in enumerate(X):
        change[e] = chr(ord('a')+index)

    for i in range(N):
        tmp = input()
        newName = ""
        for j in tmp:
            newName += change[j]
        S.append([newName, tmp])

    S.sort()

    for i in range(N):
        print(S[i][1])


main()
