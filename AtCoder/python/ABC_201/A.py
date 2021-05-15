
def juge(a):
  if a[0] == a[1] == a[2]:
    return True
  elif a[1] - a[0] == a[0] - a[2]:
    return True
  elif a[0] - a[1] == a[1] - a[2]:
    return True
  elif a[1] - a[2] == a[2] - a[0]:
    return True


def main():
  a = []
  a = input().split()
  for i in range(3):
    a[i] = int(a[i])
  if juge(a):
    print("Yes")
  else:
    print("No")

main()