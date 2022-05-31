
def main():
    N,Q = map(int,input().split())
    
    ball = [0] * N
    pos = [0] * N
    
    for i in range(N):
        ball[i] = i
    
    for i in range(N):
        pos[ball[i]] = i
        
    for qi in range(Q):
        x = int(input())
        x -= 1
        i = pos[x]
        j = i+1
        if j == N:
            j = i-1
        y = ball[j]
        ball[i],ball[j] = ball[j],ball[i]
        pos[x],pos[y] = pos[y],pos[x]
    
    for i in range(N):
        print(ball[i]+1, end=' ')
    print()
if __name__ == '__main__':
    main()