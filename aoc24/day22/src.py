import sys
from time import time
with open(sys.argv[1],'r') as f:
    D = [int(x) for x in f.read().strip().split()]
n1 = 2000
n2 = 2004
s = 0

dp = [{} for _ in D]

for i, seed in enumerate(D):
    prev, p4 = 0, [0] * 4
    for j in range(n2):
        seed = ((seed * 64)   ^ seed) % 16777216
        seed = ((seed // 32)  ^ seed) % 16777216
        seed = ((seed * 2048) ^ seed) % 16777216
        price = int(str(seed)[-1])

        p4 = p4[1:] + [price - prev]
        prev = price

        if j > 3:
            dp[i].setdefault(tuple(p4), price)
        if j + 1 == n1:
            s += seed

seen = set()
b = 0
for i, dp_row in enumerate(dp):
    for k in dp_row:
        if k not in seen:
            seen.add(k)
            b0 = sum(dp[j].get(k, 0) for j in range(len(D)))
            b = max(b, b0)

print(s)
print(b)