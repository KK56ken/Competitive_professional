import math

def main():
    H = int(input())
    
    result = math.sqrt(H*(12800000+H))
    
    print(result)
    

if __name__ == '__main__':
    main()