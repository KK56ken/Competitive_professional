K = int(input())
result = ""
while(K > 0):
    result += str((K % 2)*2)
    K = K // 2

for i in reversed(result):
    print(i,end="")
print()

# 1,10,11,100,101,110,111
# 2,20,22,200,202,220,222



