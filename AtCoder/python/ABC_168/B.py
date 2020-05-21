k = int(input())
s = input()
a = ""
flag = False
if k < len(s):
    for i in range(k):
        a = a + s[i]
    a = a + "..."
    flag = True
if flag:
    print(a)
else:
    print(s)
