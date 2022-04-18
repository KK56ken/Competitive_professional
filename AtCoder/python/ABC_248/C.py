import math

def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)

def main():
    n, m, k = map(int,input().split())
    
    result = permutations_count(m, n) - (((n+m) - k)*n)
    
    print(result)
    
main()

# 1121099407
# 126764178842844800000 - 
# 998244353


# 126987123405
# 798416518