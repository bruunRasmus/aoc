import sys
with open(sys.argv[1],'r') as f:
    D = f.read().strip()
    G = D.split('\n')
    R = len(G)
    C = len (G[0])
    starts = []
    for i in range(R):
        for j in range(C):
            if G[i][j] == '0':
                starts.append((i,j))

dirs = [(1,0),(-1,0),(0,1),(0,-1)]
def findTrail(st,part2):
    px,py = st
    if G[px][py] == '9':
        if part2 or st not in seen:
            if st not in seen: 
                seen.append((px, py))
            return 1
        return 0
    
    s= 0 
    for dx,dy in dirs:
        if 0<= px+dx < R and 0<= py+dy < C:
            if int(G[px+dx][py+dy]) == int(G[px][py]) + 1:
                s += findTrail((px+dx,py+dy),part2)       
    return s

for part2 in [False,True]:
    s = 0
    for st in starts:
        seen = []
        s += findTrail(st,part2)
    print(s)

