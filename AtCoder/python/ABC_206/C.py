import collections
from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under


def main():

  n = int(input())

  a = []
  a = list(map(int,input().split()))

  cnt = 0

  num = cmb(len(a),2)

  c = collections.Counter(a)
  print(c)
  # for i in range(1,len(c)+1):
  #   if c[i] > 1:
  #     for j in range(1,c[i]):
  #       cnt += j

  for k,v in c.items():
    if v > 1:
      for j in range(1,v):
        cnt += j
  print(num - cnt)


if __name__ == "__main__":
  main()