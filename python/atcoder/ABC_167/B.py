a, b, c, k = map(int, input().split())

suma = 0


if k > a:
    if k > a + b:
        if k == a + b + c:
            print(a - c)
        else:
            k = k - (a + b)
            print(a-k)
    else:
        print(a)
else:
    print(k)

# for i in range(k):
#     if a == 0 and b == 0:
#         suma = suma - k
#         break
#     elif a == 0 and c == 0:
#         break
#     elif b == 0 and c == 0:
#         suma = suma + k
#         break
#     if a > 0:
#         a = a - 1
#         k = k - 1
#         suma += 1
#     elif b > 0:
#         b = b - 1
#         k = k - 1
#     elif c > 0:
#         c = c - 1
#         k = k - 1
#         suma -= 1
# print(suma)
