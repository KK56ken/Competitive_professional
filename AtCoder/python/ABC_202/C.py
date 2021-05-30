def main():
  n = int(input())
  a = list(map(int,input().split()))
  b = list(map(int,input().split()))
  c = list(map(int,input().split()))
  cnt = 0

  a = list(set(a))

  for i in range(len(a)):
    for j in range(n):
      if a[i] == b[c[j]-1]:
        cnt += 1
  print(cnt)
main()