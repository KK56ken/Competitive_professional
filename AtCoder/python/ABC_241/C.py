def judge(i,j,S,N):
    
    offset = [[0,1],[1,1],[1,0],[1,-1]]
    
    for k in range(4):
        cnt = 0
        for l in range(1,6):
            if k == 3:
                if N-1 < i+offset[k][0]*l or 0 > j+offset[k][1]*l:
                    continue
            else:
                if N-1 < i+offset[k][0]*l or N-1 < j+offset[k][1]*l:
                    continue
            if S[i+offset[k][0]*l][j+offset[k][1]*l] == "#":
                cnt += 1
            if cnt == 3:
                return True
    return False


def main():
    N = int(input())
    S = []
    
    for i in range(N):
        S.append(input())

    for i in range(N):
        for j in range(N):
            if S[i][j] == "#":
                if judge(i,j,S,N):
                    print("Yes")
                    exit()
    print("No")
main()





