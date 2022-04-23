def main():
    N = int(input())
    A = list(map(int,input().split()))
    A = list(set(A))
    
    A.sort()
    
    for i in range(N):
        if i >= len(A):
            print(i)
            break
        if not A[i] == i:
            print(i)
            break
    
    
main()