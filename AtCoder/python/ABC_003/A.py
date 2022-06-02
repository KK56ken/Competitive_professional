def main():
    N = int(input())
    result = 0

    for i in range(1, N+1):
        result += 10000 * i / N
    print(int(result))


main()
