def main():
    N = int(input())
    kakudo = list(map(int,input().split()))
    result = []
    cut = []
    
    for i in range(N):
        cut.append(kakudo[i])
        for j in range(len(cut)-1):
            cut[j] = cut[j] + cut[len(cut)-1]
    
    for i in range(N):
        cut[i] = cut[i] - (cut[i] // 360) * 360
    
    cut.append(0)
    cut.append(360)
    cut.sort()
    
    for i in range(N+1):
        result.append(abs(cut[i] - cut[i+1])) 
    
    print(max(result))
    
main()
