def main():
    N, K = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    useA = [False] * N
    useB = [False] * N

    useA[0] = True
    useB[0] = True

    for i in range(1, N):
        if useA[i - 1]:
            if abs(A[i] - A[i - 1]) <= K:
                useA[i] = True
            if abs(B[i] - A[i - 1]) <= K:
                useB[i] = True

        if useB[i - 1]:
            if abs(A[i] - B[i - 1]) <= K:
                useA[i] = True
            if abs(B[i] - B[i - 1]) <= K:
                useB[i] = True
    
    if useA[N - 1] or useB[N - 1]:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
