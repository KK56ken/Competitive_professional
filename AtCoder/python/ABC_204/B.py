def main():
  n = int(input())
  a = []
  a = list(map(int,input().split()))
  suma = 0

  for i in range(n):
    if a[i] > 10:
      suma += a[i] - 10
  print(suma)
if __name__ == "__main__":
  main()