from collections import deque

lines = open("input.txt").read().strip().splitlines()
G = [[int(x) for x in list(l)] for l in lines]
R,C = len(G),len(G[0])
N = 1000
ans1 = 0
i=1

while True:
    Q = deque()
    seen= set()
    for r in range(R):
        for c in range(C):
            G[r][c] += 1
            if G[r][c] > 9: 
                Q.append((r,c))
                seen.add((r,c))
    while Q:
        r,c = Q.popleft()
        for dr in [-1,0,1]:
            for dc in [-1,0,1]:
                rr,cc = r+dr,c+dc
                if 0<=rr<R and 0<=cc<C and ((rr,cc)!= (r,c)):
                    G[rr][cc]+=1
                    if G[rr][cc] > 9 and (rr,cc) not in seen:
                        Q.append((rr,cc))
                        seen.add((rr,cc))
                        
    for (r,c) in seen:
        G[r][c] = 0
        ans1+=1
        
    if i == 100:
        print(ans1)
    
    if len(seen) == R*C:
        print(i)
        break
    i+=1                   