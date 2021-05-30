def main():
  n, k = map(int,input().split())
  friends = []
  for i in range(n):
    friends.append(list(map(int,input().split())))
  print(friends)

if __name__ == "__main__":
  main()