def main():
    A = list(map(int,input().split()))
    result = 0 
    for i in range(3):
        if i == 0:
            result = A[0]
        else:
            result = A[result]
    
    print(result)
    
main()