def main():
    N,M = map(int,input().split())

    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    
    cnt = 0
    
    for i in reversed(range(0, M)):
        for j in reversed(range(0, N-cnt)):
            if B[i] == A[j]:
                B.pop(i)
                A.pop(j)
                cnt += 1
                break

        if len(B) == 0:
            print("Yes")
            exit()

    print("No")
main()
