h, w, k = map(int, input().split())
char_c = [0] * h

for i in range(h):
    c = input()
    char_c[i] = list(c)

ans = 0
for row_bit in range(2 ** h):
    for col_bit in range(2 ** w):
        count = 0
        for row in range(h):
            if ((row_bit >> row) & 1):
                continue
            for col in range(w):
                if ((col_bit >> col) & 1):
                    continue
                #print(char_c[row][col], end='')
                if char_c[row][col] == '#':
                    count += 1
            # print()
        if count == k:
            ans += 1
print(ans)
# for i in range(h):
#     for j in range(w):
#         print(char_c[i][j], end='')
#     print()
# print(char_c)

# 2進数にするbin()
