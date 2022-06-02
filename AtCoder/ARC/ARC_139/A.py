def main():
    N = int(input())
    T = list(map(int, input().split()))

    result = bin(0)

    for i in N:
        result = result + bin(i)


main()
