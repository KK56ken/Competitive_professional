def main():
    n = int(input())
    result = "Yes"
    s = [0] * n
    t = [0] * n
    
    for i in range(n):
        s[i],t[i] = map(str, input().split())
        
        if s[i] in s and t[i] in t:
            result = "No"

    print(result)
main()