def main():
  n = int(input())
  mydict= {}

  for i in range(n):
    name, num = input().split()
    num = int(num)
    mydict[name] = num

  num = sorted(mydict.items(), key=lambda x:x[1])[-2]

  for k in mydict:
    if mydict[k] == num[1]:
      print(k)


main()