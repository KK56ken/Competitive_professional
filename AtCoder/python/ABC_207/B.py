def main():
  a,b,c,d = map(int,input().split())
  ac = 0
  i = 0

  if b >= c*d:
    print(-1)
  else:
    while(a > ac*d):
      a += b
      ac += c
      i += 1
    print(i)

if __name__ == "__main__":
  main()