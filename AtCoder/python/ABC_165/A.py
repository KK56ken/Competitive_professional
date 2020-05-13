
k = int(input())
a, b = map(int, input().split())

flag = 0
for i in range(1000):
    if (a <= k * (i+1)) and (b >= k * (i+1)):
        print("OK")
        flag = 1
        break
if flag != 1:
    print("NG")
