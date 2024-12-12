import sys
with open(sys.argv[1],'r') as f:
    D = f.read().strip()
    G = D.split('\n')
    R,C = len(G),len(G[0])


nb = [(1,0),(0,1),(-1,0),(0,-1)]

def grow_region(r,c,i):
    for dr,dc in nb:
        rr,cc = r+ dr, c + dc
        if rr in range(R) and cc in range(C) and G[rr][cc] == G[r][c]:
            regions[i][0] -= 1 #touching, so decrease perimeter count
            if (rr,cc) not in seen:
                regions[i][0] += 4 #perimeter
                regions[i][1] += 1 #area

                seen.add((rr,cc))
                regions[i][2].append((rr,cc))

                grow_region(rr,cc,i)

def sides(region):
    zr, zc = zip(*region)
    minR, minC, maxR, maxC = min(zr) - 1, min(zc) - 1, max(zr) + 1, max(zc) + 1
    
    def count_sides(dr, dc):
        count = 0
        for fixed in range(minR, maxR) if dc == 0 else range(minC, maxC):
            b = False
            for var in range(minC, maxC) if dc == 0 else range(minR, maxR):
                r, c = (fixed, var) if dc == 0 else (var, fixed)
                if (r, c) in region and (r + dr, c + dc) not in region:
                    count += not b
                    b = True
                else:
                    b = False
        return count
    
    return sum([count_sides(dr,dc) for dr,dc in nb])

seen = set()
regions = []

for r in range(R):
    for c in range(C):
        if (r,c) not in seen and r in range(R) and c in range(C):
            seen.add((r,c))
            idx = len(regions)
            regions.append([4,1,[(r,c)]])
            grow_region(r,c,idx)

s1,s2 = 0,0
for r in regions:
    s1+= r[1]*r[0]
    s2+= r[1]*sides(r[2])
print(s1,s2)
