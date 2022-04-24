def main():
    N, K = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    dp = []
    Aflag = False
    Bflag = False
    flag = False

    for i in range(N-1):
        if Aflag and Bflag:
            dp[i-1] 
            dp[i] = 

        Aflag = False
        Bflag = False

        if abs(A[i]-B[i+1]) <= K:
            Aflag = True
            dp.append(A[i])
        elif abs(A[i]-A[i+1]) <= K:
            Aflag = True
            dp.append(A[i])
        elif abs(B[i]-B[i+1]) <= K:
            Bflag = True
            dp.append(B[i])
        elif abs(B[i]-A[i+1]) <= K:
            Bflag = True
            dp.append(B[i])
        else:
            flag = True
            break
    if flag:
        print("No")
    else:
        print("Yes")


main()

# Aflag = False
#     Bflag = False
# for i in range(N):
#     if flag:
#         if abs(A[i]-A[i+1]) <= K:
#             dp.append(A[i])
#         else:
#             flag = False
# print(dp)

# dp.append(A[N-1])
# print(dp)
