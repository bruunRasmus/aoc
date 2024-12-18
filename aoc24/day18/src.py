import sys
from collections import deque

with open(sys.argv[1],'r') as f:
    D = f.read().strip().split('\n')
    bytes = [(int(x), int(y)) for x, y in (line.split(',') for line in D)]

R,C,N = (71,71,1024) if (37,68) in bytes else (7,7,12)
nb = [(0,1),(0,-1),(1,0),(-1,0)]

def bfs(m):
    path = False
    bytesM = bytes[:m]
    Q = deque([(0,0)])
    seen = set()
    dist = {(0,0):0}
    while Q:
        r,c = Q.popleft()
        if (r,c) == (R-1,C-1):
            path = True
            break
        for dr,dc in nb:
            rr,cc  = r+dr,c+dc
            if (rr,cc) not in bytesM and (rr,cc) not in seen and 0<=rr<R and 0<=cc<C:
                seen.add((rr,cc))
                dist[(rr,cc)] = dist[(r,c)] + 1
                Q.append((rr,cc))
    if not path:
        return None
    else:
        return dist[R-1,C-1]


print('part1:',bfs(N))

l,h = N,len(bytes)
while l<h:
    m = (l+h)//2
    if bfs(m):  l = m + 1
    else:       h = m
print('part2:', bytes[l-1])
