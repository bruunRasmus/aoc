import sys
from collections import deque
with open(sys.argv[1],'r') as f:
    D = f.read().strip()
    G = D.split('\n')
    R,C  = len(G), len(G[0])

    for r in range(R):
        for c in range(C):
            if G[r][c] =='S':
                start = (r,c)
            if G[r][c] == 'E':
                end = (r,c)
nb = [(0,1),(0,-1),(1,0),(-1,0)]
def bfs(G):
    Q = deque()
    dist = {start:0}
    seen = set([start])
    Q.appendleft((start,0))
    while Q:
        (r,c),d = Q.popleft()
        if (r,c) == end:
            return d,dist
        for dr,dc in nb:
            rr,cc = r+dr,c+dc
            if rr in range(R) and cc in range(C) and (rr,cc) not in seen and G[rr][cc] != '#':
                seen.add((rr,cc))
                dist[(rr,cc)] = d+1
                Q.append(((rr,cc),d+1))  
                   
P,distP = bfs(G)
s1,s2 = 0,0

for (ar, ac) in distP:
    for (br, bc) in distP:
        mhDist = abs(ar - br) + abs(ac - bc)
        chDist = distP[(ar, ac)] - distP[(br, bc)]- mhDist
        if chDist >= 100:
            if mhDist <= 2:
                s1 += 1
            if mhDist <= 20:
                s2 += 1
            
print(s1,s2)