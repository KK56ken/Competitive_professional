a, b, c, d = map(int, input().split())
flag = 0
while True:
    c = c - b
    if c <= 0:
        print("Yes")
        break
    a = a - d
    if a <= 0:
        print("No")
        break
