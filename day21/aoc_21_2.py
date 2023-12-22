import sys
from collections import deque 

f = open(sys.argv[1],'r')

stepmap = [l.rstrip() for l in f.readlines()]
R = len(stepmap)
C = len(stepmap[0])

for r in range(R):
    for c in range(C):
        if stepmap[r][c] == 'S':
            sr,sc = r,c


STEPS = 64

visited = set()
seen = set()
Q = deque([[sr,sc,0]])
while len(Q)>0:
    r,c,i = Q.pop()
    print(i)
    if i > STEPS:
        continue
    for rr,cc in [[1,0],[-1,0],[0,1],[0,-1]]:
        rrr = r + rr
        ccc = c + cc
        if 0<=rrr<R and 0<=ccc<C:
            key = (rrr,ccc,i%2)
            if i%2 == 0 and i<=STEPS:
                visited.add(key)
            if key not in seen:
                Q.append([r+rr,c+cc,i+1])
                seen.add((r+rr,c+cc,i+1))
print(len(visited))
    