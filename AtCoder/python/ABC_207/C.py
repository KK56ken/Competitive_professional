def main():

  n = int(input())
  a = []

  for i in range(n):
    a.append(list(map(int,input().split())))
    if a[i][0] == 2:
      a[i][2] = a[i][2] - 0.5
    elif a[i][0] == 3:
      a[i][1] = a[i][1] + 0.5
    elif a[i][0] == 4:
      a[i][2] = a[i][2] - 0.5
      a[i][1] = a[i][1] + 0.5
  cnt = 0

  for i in range(n):
    for j in range(i+1,n):
      cnt += max(a[i][1],a[j][1]) <= min(a[i][2],a[j][2])
  print(cnt)

if __name__ == "__main__":
  main()