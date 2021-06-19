def main():
  n = int(input())
  i = 1
  asum = 0
  while(1):
    asum += i

    if asum >= n:
      break
    i += 1
  print(i)


if __name__ == "__main__":
  main()