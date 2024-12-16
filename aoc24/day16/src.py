import sys
import heapq
with open(sys.argv[1],'r') as f:
    G = f.read().strip().split('\n')
    R,C = len(G),len(G[0])

dist = {}
prev = {}
Q = []

def min_dist(Q):
    min = 10**8
    node = None
    for n in Q:
        if dist[n]<= min:
            min = dist[n]
            node = n
    return node

nb = [(0,1),(-1,0),(0,-1),(1,0)]

def get_nbs(node):
    r,c,i = node
    dr,dc = nb[i]

    cw = (r,c,(i+1)%4) 
    ccw = (r,c,(i-1)%4)
    fw = (r+dr,c+dc,i) if G[r+dr][c+dc] != '#' else None
    return (cw,ccw,fw)
for r in range(R):
    for c in range(C):
        if G[r][c] != '#':
            for i in range(4):
                dist[(r,c,i)] = 10**8
                prev[(r,c,i)] = []
                Q.append((r,c,i))
        if G[r][c] == 'S':
            dist[(r,c,0)] = 0
        if G[r][c] == 'E':
            end = (r,c)
            
while len(Q)>0:
    node = min_dist(Q)
    Q.remove(node)
    cw,ccw,fw =  get_nbs(node)

    if dist[node] + 1000 <= dist[cw] and cw in Q:
        if dist[node] + 1000 == dist[cw]:
            prev[cw].append(node)
        else:
            dist[cw] = dist[node] + 1000 
            prev[cw] = [node]
    if dist[node] + 1000 <= dist[ccw]and ccw in Q:
        if dist[node] + 1000 == dist[ccw]:
            prev[ccw].append(node)
        else:
            dist[ccw] = dist[node] + 1000 
            prev[ccw] = [node]
    if fw and dist[node] + 1 <= dist[fw] and fw in Q:
        if dist[node] + 1 == dist[fw]:
            prev[fw].append(node)
        else:
            dist[fw] = dist[node] + 1
            prev[fw] = [node]

m = 10**8
d = []
for i in range(4):
    if dist[(*end,i)]<=m:
        if dist[(*end,i)]==m:
            d.append(i)
        m = dist[(*end,i)]
        d = [i]
print(m,d)


visited = set()
def mark(node):
    for p in prev[node]:
        visited.add((p[0],p[1]))
        mark(p)

for p in [(*end,i) for i in d]:
    mark(p)
print(len(visited)+1)



        

    

                
    



