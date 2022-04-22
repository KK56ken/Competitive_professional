def main():
    n, m, k = map(int, input().split())

    dp = [[0] * (k+1) for _ in range(n + 1)]

    dp[0][0] = 1
    mod = 998244353

    for i in range(1, n+1):
        for j in range(1, k+1):
            for l in range(max(0, j-m), j):
                dp[i][j] = (dp[i][j] + dp[i-1][l]) % mod

    print(sum(dp[n]) % mod)


main()
