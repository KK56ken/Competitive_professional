def main():
  n,k = map(int,input().split())
  num = 0
  for i in range(n):
    i += 1
    for j in range(k):
      j += 1
      num += int(str(i)+"0"+str(j))
  print(num)

if __name__ == "__main__":
  main()