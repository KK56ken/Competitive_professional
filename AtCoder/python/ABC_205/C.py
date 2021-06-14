def main():

  a, b, c = map(int,input().split())

  result = ""

  if c%2 == 0:
    if abs(a) == abs(b):
      result = "="
    elif abs(a) < abs(b):
      result = "<"
    elif abs(a) > abs(b):
      result = ">"
  else:
    if a == b:
      result = "="
    elif a < b:
      result = "<"
    elif a > b:
      result = ">"

  print(result)

if __name__ == "__main__":
  main()