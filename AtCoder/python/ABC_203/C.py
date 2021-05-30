def main():
  n, k = map(int,input().split())
  friends = []
  for i in range(n):
    friends.append(list(map(int,input().split())))
  # 進んだ村の数
  friends = sorted(friends)

  for i in range(n):
    if friends[i][0] <= k:
      k += friends[i][1]
  print(k)


if __name__ == "__main__":
  main()