from collections import deque
from math import prod

G = [list(l) for l in open("input.txt").read().strip().splitlines()]
R,C = len(G),len(G[0])
basins = []
ans1 = 0

for r in range(R):
    for c in range(C):
        valid = True
        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            rr, cc = r+dr,c+dc
            if 0<=rr<R and 0<=cc<C:
                if G[rr][cc]<=G[r][c]:
                    valid = False
        if valid:
            basins.append((r,c))
            ans1+= 1+int(G[r][c])
            
sizes = []
for lowpoint in basins:
    Q = deque([lowpoint])
    seen = set()
    while Q:
        r,c = Q.popleft()
        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            rr, cc = r+dr,c+dc
            if 0<=rr<R and 0<=cc<C and (rr, cc) not in seen:
                if G[rr][cc] != "9":
                    Q.append((rr,cc))
                    seen.add((rr,cc))
    sizes.append(len(seen))

ans2 = prod(sorted(sizes)[-3:])
print(ans1)
print(ans2)