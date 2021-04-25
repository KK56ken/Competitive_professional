
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


    result = mmin - nmin

    if result >= 0:
        print(result+1)
    else:
        print(0)


main()
