def main():
    a,b,c,d,e,f,x = map(int,input().split())
    takahashi = 0
    aoki = 0
    
    takahashi = (x // (a + c)) * a + x % (a + c)
    
    if x % (a+c) > a:
        takahashi -= x%(a+c) - a
    
    takahashi = takahashi * b
    
    aoki = (x // (d + f)) * d + x % (d + f)
    
    if x % (d+f) > d:
        aoki -= x%(d+f) - d

    aoki = aoki * e
    
    # print(takahashi, aoki)

    if takahashi > aoki:
        print("Takahashi")
    elif takahashi == aoki:
        print("Draw")
    else:
        print("Aoki")

main()