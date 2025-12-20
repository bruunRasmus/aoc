from collections import deque

lines = open("test.txt").read().strip().splitlines()
G = [list(l) for l in lines]
R,C = len(G),len(G[0])

for r in range(R):
    for c in range(C):
        if G[r][c] == "S":
            sr,sc = r,c
            G[r][c] = "."

Q = deque([(sr,sc,0,0,0)])
STEPS = 50000
seen = set()
visits = set()
while Q:
    r,c,i,qr,qc =  Q.popleft()
    if i>STEPS or (r,c,i%2,qr,qc) in seen:
        continue

    seen.add((r,c,i%2,qr,qc))
    if i%2 == 0:
        visits.add((r,c,qr,qc))
        
    for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
        rr,cc= (r+dr)%R,(c+dc)%C
        qqr,qqc = (qr+(r+dr)//R),(qc+(c+dc)//C)
        if G[rr][cc] == ".":
            Q.append((rr,cc,i+1,qqr,qqc))

print(len(visits))