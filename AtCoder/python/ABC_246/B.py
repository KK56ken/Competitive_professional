import math 

def main():
    a,b = map(int,input().split())
    d = math.sqrt(a ** 2 + b ** 2)
    
    print(a//d,b//d)

    
main()