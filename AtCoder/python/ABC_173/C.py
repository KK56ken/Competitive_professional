h, w, k = map(int, input().split())
char_c = [0] * h
damy_c = [0] * h
chcnt = 0


def check_line():
    cnt = 0
    c = 0
    for i in range(h):
        for j in range(w):
            if char_c[i][j] == "#":
                cnt += 1
    print("cnt", cnt)
    if cnt >= k + 1:
        clear_line()
        cnt = 0
        for a in range(w):
            for b in range(h):
                char_c[b][a] = "."
            if cnt >= k:
                c += 1
    else:
        c += 1
    return c


def clear_line():
    for i in range(h):
        for j in range(w):
            char_c[i][j] = damy_c[i][j]


def print_line():
    for i in range(h):
        for j in range(w):
            print(char_c[i][j])


for i in range(h):
    c = input()
    char_c[i] = list(c)
    damy_c[i] = list(c)

# print_line()

for i in range(h):
    for j in range(w):
        char_c[i][j] = "."
    chcnt = check_line()
    clear_line()

print(chcnt)
