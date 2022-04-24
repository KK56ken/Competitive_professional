import re

def main():
    S = input()
    flag = False
    
    if re.search('[A-Z]', S) and re.search('[a-z]', S):
        for i in range(len(S)):
            for j in range(len(S)):
                if i == j:
                    continue
                if S[i] == S[j]:
                    flag = True
                    break
    else:
        flag = True
    if flag:
        print("No")
    else:
        print("Yes")
main()