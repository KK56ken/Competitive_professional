import itertools

def main():
  n = int(input())
  array = map(int,input().split())

  items = list(itertools.combinations(array, 2))

  cnt = 0

  for item in items:
    if (item[0] - item[1]) % 200 == 0:
      cnt += 1
  print(cnt)
main()