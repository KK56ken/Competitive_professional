def main():

  n,k = map(int,input().split())

  cnt = 0

  while(k != cnt):
    if(n%200 == 0):
      n = n/200
    else:
      n = str(n) + "200"
    n = int(n)
    cnt += 1
  print(n)
main()