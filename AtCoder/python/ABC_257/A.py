n,x = map(int,input().split())

aru = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

if x // n == 0:
    print(aru[(x//n)])
else:
    print(aru[(x//n) + (x%n) - 1])