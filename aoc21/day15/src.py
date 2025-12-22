from math import inf
from heapdict import heapdict

lines = open("input.txt").read().strip().splitlines()
G = [[int(x) for x in list(l)] for l in lines]
R1,C1 = len(G),len(G[0])
R,C = R1*5,C1*5

dist = heapdict()
for r in range(R):
    for c in range(C):
        dist[(r,c)] = inf

dist[(0,0)] = 0
Q = [(r,c)  for r in range(R) for c in range(C)]

while dist:
    (r,c),p = dist.popitem()
    if (r,c) == (R-1,C-1):
        print(p)
    if (r,c) == (R1-1,C1-1):
        print(p)
    for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
        rr,cc = r+dr,c+dc
        if 0<=rr<R and 0<=cc<C:
            q = rr//R1 + cc//C1
            new_weight = ((G[rr%R1][cc%C1] + q)%9)
            if new_weight == 0: 
                new_weight = 9
            new_dist = p + new_weight

            if (rr,cc) in dist and dist[(rr,cc)]>new_dist:
                dist[(rr,cc)] = new_dist