n = int(input())

result = []

while(n > 0):
    if n%2 == 0 and n-1 == 1:
        result.insert(0,"A")
        n = n-1
    elif n%2 == 0:
        result.insert(0,"B")
        n = int(n/2)
    else:
        result.insert(0,"A")
        n = n-1  
for i in range(len(result)):
    print(result[i],end="")
print()