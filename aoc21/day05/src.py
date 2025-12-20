lines = open("input.txt").read().strip().splitlines()
R = C = 1000

for part2 in [False,True]:
    G = [[0 for _ in range(R) ] for _ in range(C) ]
    for l in lines:
        a,b  = l.split(" -> ")
        r1,c1 = [int(x) for x in a.split(",")]
        r2,c2 = [int(x) for x in b.split(",")]

        cmin,cmax = sorted([c1,c2])
        rmin,rmax = sorted([r1,r2])

        if rmin == rmax:
            for c in range(cmin,cmax+1):
                G[rmin][c]+=1
        elif cmin == cmax:
            for r in range(rmin,rmax+1):
                G[r][cmin]+=1
        elif part2:
            dr = 1 if r2 > r1 else -1
            dc = 1 if c2 > c1 else -1
            length = abs(r2 - r1)
            for i in range(length + 1):
                G[r1 + i * dr][c1 + i * dc] += 1

    ans = sum([1 for r in range(R) for c in range(C) if G[r][c] >1])
    print(ans)