import sys
with open(sys.argv[1],'r') as f:
    G = f.read().strip().split('\n')
    R = len(G)
    C = len(G[0])

nodes = {}
for i in range(R):
    for j in range(C):
        node = G[i][j]
        if node != '.':
            if node in nodes:
                nodes[node].append((i,j))
            else:
                nodes[node] = [(i,j)]

for part2 in [False,True]:
    s = 0
    antinodes = []
    for node in nodes.keys():
        for a in nodes[node]:
            for b in nodes[node]:
                if a != b:
                    dx,dy = a[0]-b[0], a[1]-b[1]
                    st,en = (0,R) if part2 else (1,2)
                    for i in range(st,en): #i = 1 for part 1, upper bound for part2
                        newA = a[0]+(dx*i),a[1]+(dy*i)
                        newB = b[0]-(dx*i),b[1]-(dy*i)
                        if newA not in antinodes and 0<=newA[0]<R and 0<=newA[1]<C :
                            antinodes.append(newA)
                            s+=1
                        if newB not in antinodes  and 0<=newB[0]<R and 0<=newB[1]<C:
                            antinodes.append(newB)
                            s+=1
    print(s)

            


