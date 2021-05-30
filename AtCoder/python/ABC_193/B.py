
def main():
  n = int(input())

  min_price = 10000000000000
  flg = False

  for i in range(n):
    a, p, x = map(int, input().split())
    x -= a
    if x > 0:
      if min_price > p:
        flg = True
        min_price = p
    else:
      continue
  if flg:
    print(min_price)
  else:
    print(-1)

if __name__ == "__main__":
  main()