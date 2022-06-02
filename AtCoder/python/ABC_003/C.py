def main():
    N, K = map(int, input().split())
    R = list(map(int, input().split()))

    R.sort()

    point = 0

    for i in range(N-K, N):
        point = (point+R[i])/2

    print(point)


main()
