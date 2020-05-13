n = int(input())
a = []
cnt = 0

for i in range(n):
    q = input()
    if not q in a:
        a.append(q)
        cnt += 1

print(cnt)
