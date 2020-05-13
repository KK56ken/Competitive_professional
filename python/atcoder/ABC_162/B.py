n = int(input())
suma = 0
for i in range(1, n+1):
    if not (i % 3 == 0 and i % 5 == 0 or i % 3 == 0 or i % 5 == 0):
        suma = i + suma
    # print(suma)
print(suma)
