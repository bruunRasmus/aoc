import sys

with open(sys.argv[1],'r') as f:
    D = f.read().strip().split('\n')
    bytes = []
    for l in D:
        x,y = l.split(',')
        bytes.append((int(x),int(y)))

def min_dist(Q):
    min_dist,min_node = 10**8,None
    for node in Q:
        if dist[node]< min_dist:
            min_dist = dist[node]
            min_node = node
    return min_node

def reset(bytesM):
    for r in range(R):
        for c in range(C):
            if (r,c) not in bytesM:
                dist[(r,c)] = 10**8
                prev[(r,c)] = None
    dist[(0,0)] = 0

R,C = (71,71) if (37,68) in bytes else (7,7)
nb = [(0,1),(0,-1),(1,0),(-1,0)]
l,h = 1024, len(bytes)
while l<h:
    m = (l+h)//2
    bytesM = bytes[:m]
    dist = {}
    prev = {}
    Q = [(0,0)]
    reset(bytesM)
    
    while Q:
        r,c = min_dist(Q)
        Q.remove((r,c))
        if (r,c) == (R-1,C-1):
            break
        for dr,dc in nb:
            rr,cc = r+dr, c + dc
            if (rr,cc) not in bytesM and rr in range(R) and cc in range(C):
                alt = dist[(r,c)] + 1
                if alt < dist[(rr,cc)]:
                    dist[(rr,cc)] = alt
                    prev[(rr,cc)] = (r,c)
                    Q.append((rr,cc))
    if prev[(R-1,C-1)]:
        print(f'path with {m} bytes')
        l = m + 1
    else:
        print(f'no path with {m} bytes')
        h = m

print('m;',bytes[m])