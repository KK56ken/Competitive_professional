n, m, x = map(int, input().split())
book = []
sum10 = []

for i in range(n):
    book.append(input().split())
a = len(book)

for k in range(m+1):
    for i in range(m ** a):
        lean = []
        total = 0
        print("pattern {}: ".format(i), end="")
        for j in range(1, n):  # このループが一番のポイント
            if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
                lean.append(int(book[j][k]))  # フラグが立っていたら bag に果物を詰める
                total += int(book[j][0])
        if sum(lean) >= x:
            sum10.append(total)

print(sum10)

# for i in range(n):
#     for j in range(1,m+1):
#         book[j][i]

# print(n, m, x)
# print(book)
