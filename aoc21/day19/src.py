from collections import defaultdict
blocs = open("input.txt").read().strip().split("\n\n")

scanners = []
for b in blocs:
    scanners.append([[int(x) for x in l.split(",")] for l in b.splitlines()[1:]])
S = len(scanners)    

def adjustment(si,sj):
    counter = defaultdict(int)
    for perm in [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]:
        for signs in [[1,1,1],[1,1,-1],[1,-1,1],[1,-1,-1],
                      [-1,1,1],[-1,1,-1],[-1,-1,1],[-1,-1,-1]]:
            for bj in sj:
                bj = [bj[perm[l]]*signs[l] for l in range(3)]
                for bi in si:       
                    offsets = tuple([bj[l]-bi[l] for l in range(3)])
                    counter[offsets] += 1
                    if counter[offsets] == 12:
                        return offsets,perm,signs
    return None,None,None
                
def transform(b,offsets,perm,signs):
    return [b[perm[l]]*signs[l] - offsets[l] for l in range(3)]
    
Q = {0}
known = {0}
adjusted_beacons = {0:scanners[0]}
scanner_pos = [(0,0,0)]

while Q:
    i = Q.pop()
    bi = adjusted_beacons[i]
    for j in range(S):
        if j in known:
            continue
        bj = scanners[j]
        o,p,s = adjustment(bi,bj)
        if o:
            scanner_pos.append(o)
            adjusted_beacons[j] = [transform(b,o,p,s) for b in bj]
            Q.add(j)
            known.add(j)
            
relative_beacons = set()
for i in adjusted_beacons:
    for b in adjusted_beacons[i]:
        relative_beacons.add(tuple(b))

max_dist = 0
for s1 in scanner_pos:
    for s2 in scanner_pos:
        max_dist = max(max_dist,sum(abs(s2[d]-s1[d]) for d in range(3)))
        

print(len(relative_beacons))
print(max_dist)