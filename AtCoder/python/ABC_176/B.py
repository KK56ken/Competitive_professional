n = input()
suma = 0
for i in range(len(n)):
    suma += int(n[i])
if suma % 9 == 0:
    print("Yes")
else:
    print("No")
