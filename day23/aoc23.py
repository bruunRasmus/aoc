import sys
from collections import deque
f = open(sys.argv[1],'r')

trails = [l.rstrip() for l in f]
R = len(trails)
C = len(trails[0])

Q = deque()

for c in range(C):
    if trails[0][c] == '.':
        start = [0,c,0,0]
    if trails[R-1][c] == '.':
        end = [R-1,c]
print(f"end coord = {end}")
Q.append(start)
visited = {(r,c):[-1]*4 for r in range(R) for c in range(C)}
endLengths = []
#possibleChoices = deque(range(100))
dirs = [[0,1],[1,0],[0,-1],[-1,0]]

while len(Q) > 0:
    r,c,prevdir,l = Q.popleft()
    if trails[r][c] =='#':
        print("hastag",r,c)
    #if sum([i[:len(x)]==x for x din visited[r,c]]):
    #print(visited[(r,c)][prevdir])
    if visited[(r,c)][prevdir]>=l:
        continue
    else:
        visited[(r,c)][prevdir] = l

    #if [r,c] == end:
    #    visited[(r,c)][prevdir] = ((l,prevdir))
        #print(i)  
        #print(f'lenght = {l},\t path = {i}')
        #endLengths.append(l)
        #print(f"A path ended in {l} steps")
        #continue
    #print(visited[(r,c)])
    #visited[(r,c)].add((l,prevdir))
    #inc = 0
    #slip = ['>', 'v', '<', '^'][prevdir]
    #f trails[r][c] in ['>', 'v', '<', '^']:
    #    i = i+[trails[r][c],r,c]
    #    for j in range(4):
    #        rr,cc  = dirs[j]   
            #print(r+rr,c+cc,abs(prevdir-j),trails[r+rr][c+cc])
    #        if 0<=r+rr<R and 0<=c+cc<C and trails[r+rr][c+cc] != '#':#and abs(prevdir-j)!= 2:
    #            Q.append([r+rr,c+cc,j,l+1,i])
        #print(f'after:\t {i}')
        #Q.append([r+rr,c+cc,prevdir,l+1,i])
    #    continue
    for j in range(4):
        rr,cc  = dirs[j]   
        #print(r+rr,c+cc,abs(prevdir-j),trails[r+rr][c+cc])
        if 0<=r+rr<R and 0<=c+cc<C and trails[r+rr][c+cc] != '#':#and abs(prevdir-j)!= 2:
            Q.append([r+rr,c+cc,j,l+1])
    #print(len(Q))

print(endLengths)