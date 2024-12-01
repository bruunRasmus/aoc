import sys
from collections import deque
from collections import defaultdict
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
    #slip = ['>', 'v', '<', '^'][prevdir]
    if (r,c) == end:
        V.append(end)
        E[node].append((end,l+1))
    elif trails[r][c] in ['>', 'v', '<', '^']:
        i = ['>', 'v', '<', '^'].index(trails[r][c])
        rr,cc = dirs[i]
        #if trails[r][c] == slip:
        if (r,c)!= node:
            E[node].append([(r,c),l+1])
        #rr,cc = dirs[prevdir]
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

fromE = {v:[] for v in V}

for e in E:
    for next in E[e]:
        E[next[0]].append((e,next[1]))
        #fromE[next[0]] = fromE[next[0]] + [e]


#print("fromE:",fromE)
Q = deque()
Q.append([start,start,0,[]])


visited = {v:[] for v in V}
#visited = {v:{vv:-1 for vv in fromE[v]} for v in V}
#visited[start][start] = -1
#print("visited:",visited)
endLengths = 0

while len(Q)>0:
    currVertex,prevVertex,l,i = Q.popleft()
    if currVertex in i :
        continue
    else:
        i = i + [currVertex]

    if currVertex == end:
        #visited[currVertex].append(i)
        #print(i)  
        print(f'lenght = {l},\t path = {i}')
        endLengths = max(endLengths,l)
        print(f"A path ended in {l} steps")
        continue

    for next in E[currVertex]:
        #pass
        #print(next[0])
        Q.append((next[0],currVertex,l+next[1],i))
print(endLengths)








