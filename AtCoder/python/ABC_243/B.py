def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    
    kanzen = 0
    hukanzen = 0
    
    for i in range(N):
        for j in range(N):
            if i == j and A[i] == B[j]:
                kanzen += 1
            elif A[i] == B[j]:
                # print("a",A[i],B[j],i,j)
                hukanzen += 1
    
    print(kanzen)
    print(hukanzen)

if __name__ == '__main__':
    main()