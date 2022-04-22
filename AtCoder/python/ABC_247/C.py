
def saiki(n):
    if n == 1:
        return [1]
    else:
        return saiki(n-1) + [n] + saiki(n-1)
        

def main():
    n = int(input())
    result = saiki(n)
    
    print(result)
    
main()