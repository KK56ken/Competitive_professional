def main():
    n = int(input())
    dp = [0] * n

    scaffold = list(map(int, input().split()))

    for i in range(1, n):
        if i == 1:
            dp[i] = abs(scaffold[i] - scaffold[i-1])
        else:
            dp[i] = min(abs(scaffold[i] - scaffold[i-1])+dp[i-1],
                        abs(scaffold[i]-scaffold[i-2])+dp[i-2])
    print(dp[n-1])


main()
