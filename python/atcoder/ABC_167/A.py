

s = input()
t = input()
flag = 0
for i in range(len(s)):
    if s[i] != t[i]:
        print("No")
        flag = 1
        break

if flag != 1:
    print("Yes")
