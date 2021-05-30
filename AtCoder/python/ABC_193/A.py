
def main():
  a, b = map(int,input().split())
  c = b / a
  ans = 1 - c
  print(round(ans*100,5))

if __name__ == "__main__":
  main()