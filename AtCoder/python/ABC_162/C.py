import math
from functools import reduce


def gcd(*numbers):
    return reduce(math.gcd, numbers)


k = int(input())
suma = 0

for i in range(1, k+1):
    for j in range(1, k+1):
        for l in range(1, k + 1):
            suma += gcd(i, j, l)


print(suma)
