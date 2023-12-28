import sys
from collections import deque
f = open(sys.argv[1],'r')

trails = [l.rstrip() for l in f]
R = len(trails)
C = len(trails[0])

Q = deque()
for c in range(C):
    if trails[0][c] == '.':
        start = (0,c)
    if trails[R-1][c] == '.':
        end = (R-1,c)
        
V = [start]
E = {start:[],end:[]}     

Q.append((start,1,0,start))
dirs = [[0,1],[1,0],[0,-1],[-1,0]]
visited = []
print(end)
while len(Q)>0:
    [r,c],prevdir,l,node = Q.popleft()
    visited.append((r,c,node))
    slip = ['>', 'v', '<', '^'][prevdir]
    if (r,c) == end:
        V.append(end)
        E[node].append((end,l+1))
    
    elif trails[r][c] in ['>', 'v', '<', '^']:
        if trails[r][c] == slip:
            E[node].append([(r,c),l+1])
            rr,cc = dirs[prevdir]
            if (r,c) not in V:
                V.append((r,c))
                E[(r,c)] = []
                Q.append(([r+rr,c+cc],j,0,(r,c)))
    else:
        for j in range(4):
            rr,cc  = dirs[j]   
            if 0<=r+rr<R and 0<=c+cc<C and trails[r+rr][c+cc] != '#':#
                if (r+rr,c+cc,node) not in visited:
                    Q.append(([r+rr,c+cc],j,l+1,node))

for  e in E:
    print(e,':',E[e])


Qp = deque(V)
distance = {v:-10e6 for v in V}
print(Qp)
def longestPaths(s,t,E):
    distance[s] = 0
    while len(Qp) > 0:
        node = Qp.popleft()

        if distance[node] != -10e6:

            for neighbour,weight in E[node]:
                new_dist = distance[node] + weight
                distance[neighbour] = max(distance[neighbour],new_dist)
    print(distance)
    return  distance[t]

print(longestPaths(start,end,E))


