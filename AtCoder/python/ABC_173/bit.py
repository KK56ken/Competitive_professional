h, w, k = map(int, input().split())
char_c = [0] * h

for i in range(h):
    c = input()
    char_c[i] = list(c)

ans = 0
for i in range(2 ** h):
    row_list = []
    row_list.append(bin(i))
    for j in range(2 ** w):
        count = 0
        col_list = []
        col_list.append(bin(j))
        for row in range(h):
            if row_list[row]:
                continue
            try:
                print(hoge[2])
            except:
                None
            for col in range(w):
                if col < len(col_list):
                    continue
                print(char_c[row][col], end='')
                if char_c[row][col] == '#':
                    count += 1
            print()
        if count == k:
            ans += 1
print(ans)
# for i in range(h):
#     for j in range(w):
#         print(char_c[i][j], end='')
#     print()
# print(char_c)

# 2進数にするbin()
