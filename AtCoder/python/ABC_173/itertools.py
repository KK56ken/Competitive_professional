import itertools
ans = 0
for i in itertools.product([0, 1], repeat=10):
    if sum(i) == 5:
        ans += 1
print(ans)
# 252
