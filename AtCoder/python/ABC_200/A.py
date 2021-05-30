def main():
  n = int(input())

  if 100 >= n:
    print(1)
  else:
    if int(n%100) == 0:
      print(int(n/100))
    else:
      print(int(n / 100)+1)

main()