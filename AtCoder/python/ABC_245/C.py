def main():
    N, K = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    Aflag = False
    Bflag = False
    flag = False
    eflag = False
    

    for i in range(N-1):
        if Aflag and not Bflag:
            if abs(A[i]-A[i+1]) <= K:
                Aflag = True
                Bflag = True
            elif abs(A[i]-B[i+1]) <= K:
                Aflag = True
                Bflag = True
            else:
                Aflag = False
                Bflag = False
            
            eflag = True
                
        elif Bflag and not Aflag:
            if abs(B[i]-A[i+1]) <= K:
                Aflag = True
                Bflag = True
            elif abs(B[i]-B[i+1]) <= K:
                Aflag = True
                Bflag = True
            else:
                Aflag = False
                Bflag = False
            eflag = True
        
        if not eflag: 
            if Aflag or i == 0:
                if abs(A[i]-A[i+1]) <= K:
                    Aflag = True
                elif abs(B[i]-A[i+1]) <= K:
                    Aflag = True
                else:
                    Aflag = False

            if Bflag or i == 0:
                if abs(B[i]-B[i+1]) <= K:
                    Bflag = True
                elif abs(A[i]-B[i+1]) <= K:
                    Bflag = True
                else:
                    Bflag = False
        eflag = False
        # print()
        # print("i=",i)
        # print(abs(A[i]-A[i+1]),abs(B[i]-A[i+1]))
        # print(abs(B[i]-B[i+1]),abs(A[i]-B[i+1]))
        # print("Aflag=",Aflag)
        # print("Bflag=",Bflag)
        # print("A[",i,"]=",A[i])
        # print("B[",i,"]=",B[i])
        
        
        if not Aflag and not Bflag:
            flag = True
            break
        
    if flag:
        print("No")
    else:
        print("Yes")
main()