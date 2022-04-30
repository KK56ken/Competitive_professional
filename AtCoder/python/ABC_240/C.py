def main():
    N,X = map(int,input().split())
    
    for _ in range(N):
        a, b = map(int,input().split())
        if X-a == 0 or X-b == 0:
            print("Yes")
            exit()
        X = X-min(a,b)
        print(X)
        
    print("No")
            
    
    
if __name__ == '__main__':
    main()