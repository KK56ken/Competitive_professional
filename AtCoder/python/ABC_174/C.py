k = int(input())
s = 7
s = s % k
cnt = 0
if k % 2 == 1 and not k % 5 == 0:
    while(1):
        if s == 0:
            cnt += 1
            print(cnt)
            break
        else:
            s = (s * 10 + 7) % k
            cnt += 1
else:
    print(-1)



