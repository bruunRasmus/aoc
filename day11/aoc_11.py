import sys
f = open(sys.argv[1],'r')

galaxy= [[c for c in l.rstrip()] for l in f]

def expand(galaxy,dim,exp = [[],[]]):    
    for i,l in enumerate(galaxy):
        if '#' not in l:
            exp[dim].append(i)
    return exp

galaxyExp  = expand(zip(*galaxy),1,expand(galaxy,0))
gIdx = [[i,j] for j in range(len(galaxy[0])) for i in range(len(galaxy)) if galaxy[i][j] == '#' ]

s = 0
for g in gIdx:
    for gg in gIdx:
        xmin,xmax = min(g[0],gg[0]),max(g[0],gg[0])
        ymin,ymax = min(g[1],gg[1]),max(g[1],gg[1])

        offset = 0
        for x in range(xmin,xmax):
            if x in galaxyExp[0]:
                offset += 1000000 -1 #replace with 1 for part 1
        for y in range(ymin,ymax):
            if y in galaxyExp[1]:
                offset += 1000000 -1
                
        s += (xmax-xmin) + (ymax-ymin) + offset
print(s/2)