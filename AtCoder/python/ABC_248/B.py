def main():
    a,b,k = map(int,input().split())
    
    cnt = 0
    
    while(a < b):
        a = a * k
        cnt += 1
    
    print(cnt)
    
main()