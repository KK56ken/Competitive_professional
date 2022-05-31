s = input()
cnt = 0
flag = True

for i in range(len(s)//2):
    # if s[i] != s[len(s)-1-i]:
    #     print("No")
    #     exit()
    if s[len(s)-1-i] == "a" and flag:
        cnt += 1
    else:
        flag = False
        break

for i in range(cnt):
    s = "a" + s

for i in range(len(s)//2):
    if s[i] != s[len(s)-1-i]:
        print("No")
        exit()

print("Yes")