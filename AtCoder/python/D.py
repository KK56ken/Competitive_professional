import math


def main():

    n = int(input())
    a = list(map(int, input().split()))

    q = int(input())

    a.sort()

    for _ in range(q):
        l, r, x = map(int, input().split())

        ok = r
        ng = l

        while(ok-ng > 1):
          i = (ok+ng) // 2




main()



2, 3, 4, 5, 6

