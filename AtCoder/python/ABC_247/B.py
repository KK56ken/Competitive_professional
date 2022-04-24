def main():
    n = int(input())
    result = "Yes"
    s = [0] * n
    t = [0] * n
    sflag = False
    tflag = False

    for i in range(n):
        s[i], t[i] = map(str, input().split())

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if s[i] == s[j] or s[i] == t[j]:
                sflag = True
            if t[i] == t[j] or t[i] == s[j]:
                tflag = True

        if sflag and tflag:
            result = "No"
            break

    print(result)


main()
