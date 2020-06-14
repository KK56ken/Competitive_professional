
n = []

n = input().split()

for i in range(5):
    n[i] = int(n[i])

for i in range(5):
    if n[i] == 0:
        print(i+1)
