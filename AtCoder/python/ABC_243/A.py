def main():
    V,A,B,C = map(int,input().split())
    
    N = 0
    
    while(V >= 0):
        if N == 0:
            V -= A
            if V < 0:
                print("F")
            N += 1
        elif N == 1:
            V -= B
            if V < 0:
                print("M")
            N += 1
        elif N == 2:
            V -= C
            if V < 0:
                print("T")
            N = 0
main()