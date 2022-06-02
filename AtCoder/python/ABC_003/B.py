def judge(i, S):
    e = ['a', 't', 'c', 'o', 'd', 'e', 'r']
    for j in range(len(e)):
        if S[i] == e[j]:
            return True

    return False


def main():
    S = input()
    T = input()
    flag = True

    for i in range(len(S)):
        if S[i] == T[i]:
            continue
        elif S[i] == '@':
            if judge(i, T):
                continue
            else:
                flag = False
                break

        elif T[i] == '@':
            if judge(i, S):
                continue
            else:
                flag = False
                break
        else:
            flag = False
            break

    if flag:
        print("You can win")
    else:
        print("You will lose")


main()
