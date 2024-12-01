import sys
from collections import deque
f = open(sys.argv[1],'r')

trails = [l.rstrip() for l in f]
R = len(trails)
C = len(trails[0])

Q = deque()

for c in range(C):
    if trails[0][c] == '.':
        start = [0,c,0,0,[0]]
    if trails[R-1][c] == '.':
        end = [R-1,c]
print(f"end coord = {end}")
Q.append(start)
visited = {(r,c):[] for r in range(R) for c in range(C)}
endLengths = []
#possibleChoices = deque(range(100))
dirs = [[0,1],[1,0],[0,-1],[-1,0]]
while len(Q) > 0:
    r,c,prevdir,l,i = Q.popleft()
    if trails[r][c] =='#':
        print(r,c)
    if sum([i[:len(x)]==x for x in visited[r,c]]):
        #print(f"path {i} ended by selfloop after {l} steps")
        continue
    if [r,c] == end:
        visited[(r,c)].append(i)    
        print(f'lenght = {l},\t path = {i}')
        endLengths.append(l)
        #print(f"Path {i} ended in {l} steps")
        continue
    #print(visited[(r,c)])
    visited[(r,c)].append(i)
    inc = 0
    slip = ['>', 'v', '<', '^'][prevdir]
    if trails[r][c] in ['>', 'v', '<', '^']:
        if trails[r][c] == slip:
            rr,cc = dirs[prevdir]
            #print("ici")
            #print(f'before:\t {i}')
            #print(r,c)
            i = i+[slip,r,c]
            #print(f'after:\t {i}')
            Q.append([r+rr,c+cc,prevdir,l+1,i])
        continue
    for j in range(4):
        rr,cc  = dirs[j]   
        #print(r+rr,c+cc,abs(prevdir-j),trails[r+rr][c+cc])
        if 0<=r+rr<R and 0<=c+cc<C and trails[r+rr][c+cc] != '#':#and abs(prevdir-j)!= 2:
            Q.append([r+rr,c+cc,j,l+1,i])
    #print(len(Q))

print(endLengths)