import sys
with open(sys.argv[1],'r') as f:
    G = f.read().strip().split('\n')

slopes = [(1,1),(1,3),(1,5),(1,7),(2,1)]
p = 1
for r0,c0 in slopes:
    s = 0
    for i in range(len(G)//r0):
        r,c = r0*i,c0*i
        s+= G[r][c%len(G[0])] == '#'
    if (r0,c0) ==(1,3):
        print(s)
    p*=s
        
print(p)