n = int(input())
p = list(map(int,input().split()))

result = [0]*10000000
for i in range(n):
    result[p[i]-1] = i+1
result = list(dict.fromkeys(result))

result.remove(0)
for r in result:
    print(r, end=" ")
print()

