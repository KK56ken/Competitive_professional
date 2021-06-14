
def nibutan(data, n):
  left = 0
  right = len(data) - 1

  while left <= right:
    mid = int((left + right) / 2)
    if data[mid] == n:
      return data[mid]
    elif data[mid] < n:
      left = mid + 1
    else:
      right = mid - 1
  return -1

def main():
  a = [1,2,4,5,6,9]
  n = 4

  print(nibutan(a, n))


if __name__ == "__main__":
  main()
