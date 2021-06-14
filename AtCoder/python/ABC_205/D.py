def main():

  n, q = map(int,input().split())

  a = []
  b = []
  result = []

  a = list(map(int,input().split()))
  i = 1
  while(a[n-1] != i):
    if not i in a:
      b.append(i)
    i += 1

  # print(b)

  for i in range(q):
    k = int(input())
    try:
      result.append(b[k-1])
    except IndexError:
      result.append(k + len(a))


  for i in range(q):
    print(result[i])

if __name__ == "__main__":
  main()