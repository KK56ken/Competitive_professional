h, w = map(int, input().split())
h0, w0 = map(int, input().split())
h0 = h0 - 1
w0 = w0 - 1
nmap = [[0] * w for i in range(h)]
place = []
for _ in range(h):
    place.append(input())

for i in range(h):
    for j in range(w):
        nmap[i][j] = place[i][j]

n = 0
cnt = 0
while h0 < h and w0 < w and h0 > 0 and w0 > 0 and cnt != 2000:
    if nmap[h0][w0] == ".":
        nmap[h0][w0] = "*"
        if n == 0:
            h0 = h0
            w0 = w0 + 1
            n = 1
        elif n == 1:
            h0 = h0 + 1
            w0 = w0
            n = 2
        elif n == 2:
            h0 = h0
            w0 = w0 - 1
            n = 3
        elif n == 3:
            h0 = h0 - 1
            w0 = w0
            n = 0
    elif nmap[h0][w0] == "*":
        nmap[h0][w0] = "."
        if n == 0:
            h0 = h0
            w0 = w0 - 1
            n = 3
        elif n == 1:
            h0 = h0 - 1
            w0 = w0
            n = 0
        elif n == 2:
            h0 = h0
            w0 = w0 + 1
            n = 1
        elif n == 3:
            h0 = h0 + 1
            w0 = w0
            n = 2
    cnt += 1

for i in range(h):
    for j in range(w):
        print(nmap[i][j], end="")
    print()
