n = int(input())
array = input().split()
difference = 0
suma = 0

for i in range(len(array)):
    array[i] = int(array[i])

for i in range(1, len(array)):
    if array[i-1] > array[i]:
        difference = array[i - 1] - array[i]
        array[i] += difference
        suma += difference
print(suma)
