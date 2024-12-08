import sys
with open(sys.argv[1],'r') as f:
    grid = f.read().strip().split('\n')
    R = len(grid)
    C = len(grid[0])
    for i in range(R):
        for j in range(C):
            if grid[i][j] == '^':
                pos = (j,i)

def sim(pos,obs):
    visited_dir = {}
    dirs = [[0,-1],[1,0],[0,1],[-1,0]] 
    k = 0
    while (0<=pos[0]<C and 0<=pos[1]<R):
        dir = dirs[k]
        if pos in visited_dir.keys():
            if k in visited_dir[pos]:
                return (1,visited_dir) #position and direction seen before: Loop
            else:
                visited_dir[pos].append(k)
        else:
            visited_dir[pos] = []
        
        nx,ny = [pos[0]+dir[0],pos[1]+dir[1]]
        if 0<=nx<C and 0<=ny<R and (grid[ny][nx] =='#' or (nx,ny) == obs):
            k = (k+1)%4
        else:
            pos = (nx,ny)
    return (-len(visited_dir.keys()),visited_dir.keys())

s1,course  = sim(pos,None)
s2 = 0
for i in range(R):
    for j in range(C):
        if (i,j) in course:
            v = sim(pos,(i,j))[0]
            if v == 1:
                s2+=1
print(-s1,s2)