def has_duplicates(seq):
    return len(seq) != len(set(seq))

def main():
  n = int(input())
  a = []
  a = list(map(int,input().split()))

  result = ""
  if has_duplicates(a):
    result = "No"
  else:
    result = "Yes"

  print(result)

if __name__ == "__main__":
  main()