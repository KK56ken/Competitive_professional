def main():
  n, k = map(int,input().split())
  a = []
  for i in range(n):
    a.append(list(map(int,input().split())))
  L = k*k/2+1

  wa = -1
  ac = 100000000
  while wa + 1 < ac:
    wj = (wa + ac) / 2
    ok = False
    s = [[0] * (n+1)] * (n+1)
    for i in range(n):
      for j in range(n):
        if a[i][j]>wj:
          s[i+1][j+1] = 1
        else:
          s[i+1][j+1] = 0

    for i in range(n+1):
      for j in range(n):
        s[i][j+1] += s[i][j]

    for i in range(n+1):
      for j in range(n):
        s[i+1][j] += s[i][j]

    for i in range(n-k+1):
      for j in range(n-k+1):
        now = s[i+k][j+k]
        now -= s[i][j+k]
        now -= s[i+k][j]
        now += s[i][j]
        if now < L: ok = True

    if ok:
      ac = wj
    else:
      wa = wj
  print(ac)


if __name__ == "__main__":
  main()