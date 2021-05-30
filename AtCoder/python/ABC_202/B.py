def main():
  s = input()
  new_s = list(reversed(s))

  for i in range(len(new_s)):
    if new_s[i] == "9":
      new_s[i] = "6"
    elif new_s[i] == "6":
      new_s[i] = "9"


  new_str = ''.join(new_s)
  print(new_str)

main()