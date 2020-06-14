
k = 0
t = 0

x, y = map(int, input().split())


if y % 2 == 1:
    print("No")
else:
    y2 = y / 2
    k = abs(x - y2)
    # print("k=", k)

    n = abs(4 * k - k)
    m = abs(x - y)
    t = abs(n - m)
    # print("n=", n)
    # print("m=", m)
    # print("t=", t)
    if k + t == x:
        print("Yes")
    else:
        print("No")
