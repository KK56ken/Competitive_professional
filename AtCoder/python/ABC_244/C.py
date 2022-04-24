def main():
    N = int(input())
    result = 1
    l = list(range(1,2*N+2))
    turn = True
    cnt = 0

    while(result != 0):
        if turn:
            print(l[0],flush=True)
            result = l[0]
            l.pop(0)
            turn = False
            cnt += 1
            
        else:
            if len(l) != 0:
                result = int(input())
                l.pop(result-(cnt+1))
                turn = True
                cnt += 1
            else:
                result = 0
main()