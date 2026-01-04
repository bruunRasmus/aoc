cucumbers = open("input.txt").read().strip().splitlines()
G = [list(l) for l in cucumbers]
R,C = len(G),len(G[0])
i = 0
while True:
    M = 0
    for cucumber,(dr,dc) in [(">",(0,1)),("v",(1,0))]:
        moved = moved_from = set()
        for r in range(R):
            for c in range(C):
                if G[r][c] == cucumber and (r,c) not in moved:
                    rr,cc = (r+dr)%R,(c+dc)%C
                    if G[rr][cc] == "." and (rr,cc) not in moved_from:
                        G[r][c] = "."
                        G[rr][cc] = cucumber
                        moved.add((rr,cc))
                        moved_from.add((r,c))
        M += len(moved)
    i+=1
    if not M:
        break
print(i)