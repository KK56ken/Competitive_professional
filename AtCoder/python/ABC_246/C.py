def main():
    n, k, x = map(int, input().split())
    end = False

    a = list(map(int, input().split()))

    list.sort(a, reverse=True)
    for i in range(n):

        if a[i] >= x:
            use = a[i] // x
            k = k - use
            a[i] = a[i] - x * use
        if k <= 0:
            end = True
            break

    if not end:
        list.sort(a, reverse=True)
        for i in range(n):
            if a[i] > 0:
                a[i] = max(a[i] - x, 0)
                k -= 1
            if k <= 0:
                break

    if k < 0:
        print(sum(a) - x * k)
    else:
        print(sum(a))


main()
