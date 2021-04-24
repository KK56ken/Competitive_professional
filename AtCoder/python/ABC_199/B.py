
def main():
    n = int(input())
    nmin = 10000
    mmin = 10000
    one_liner = []
    one_liner = input().split()
    tow_liner = input().split()

    for i in range(n):
        one_liner[i] = int(one_liner[i])
        tow_liner[i] = int(tow_liner[i])

    nmin = max(one_liner)
    mmin = min(tow_liner)

    for i in range(n):
        num = abs(one_liner[i] - tow_liner[i])

    result = abs(nmin - mmin)

    if num == 0:
        print(0)
    elif result == 0:
        print(result)
    else:
        print(result+1)


main()
