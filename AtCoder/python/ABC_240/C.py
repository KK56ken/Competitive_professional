def main():
    N,X = map(int,input().split())
    dp = [[] for _ in range(N+1)]
    
    dp[0].append(0)
    
    for i in range(1,N+1):
        a, b = map(int,input().split())
        for j in range(len(dp[i-1])):
            if dp[i-1][j]+a <= X:
                dp[i].append(dp[i-1][j]+a)
            if dp[i-1][j]+b <= X:
                dp[i].append(dp[i-1][j]+b)
        dp[i] = list(set(dp[i]))
    if X in dp[i]:
        print("Yes")
        exit()

    print("No")

if __name__ == '__main__':
    main()