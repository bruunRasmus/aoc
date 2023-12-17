import sys
from heapq import heapify, heappop,heappush
f = open(sys.argv[1],'r')
heatmap = f.read().strip().split('\n')
heatmap = [[int(c) for c in l ] for l in heatmap]

R= len(heatmap)
C = len(heatmap[0])

Q = []
dist = {}
prev = {}
for indir in range(4):
    for l in range(10):
        for c in range(len(heatmap[0])):
            for r in range(len(heatmap)):
                dist[(r,c,l,indir)] = 1e10

for i in range(4):
    dist[(0,0,0,i)] = 0
    heappush(Q,(0,(0,0,0,1)))

def neighbour(x,d,l):
    c,r = x
    ns =  [(c+1,r,1),(c-1,r,3),(c,r+1,0),(c,r-1,2)]
    ns = [(cc,rr,dd,(l+1)) if d==dd else (cc,rr,dd,0) for cc,rr,dd in ns]
    ns = [(cc,rr,dd,ll) for cc,rr,dd,ll in ns if ((d==dd) or (l >= 3))] #part2, can only turn after 3
    ns = [(cc,rr,dd,ll) for cc,rr,dd,ll in ns if not(cc == C-1 and rr == R-1 and ll<3)] #part2, can't end on l<3
    return ns
    
qelm = {}
while len(Q)>0:
    d,q = heappop(Q)
    r,c,l,d = q
    if (([r,c] == [len(heatmap)-1,len(heatmap[0])-1])):
        break
    for n in neighbour((c,r),d,l):
        cc,rr,dd,ll = n
        if 0<=cc<C and 0<=rr<R and ll < 10 and abs(dd-d)!=2: #can't turn back, ll<3 for part 1
            alt = dist[(r,c,l,d)] + heatmap[r][c]
            k = (rr,cc,ll,dd)
            if  alt < dist[k]:
                dist[(rr,cc,ll,dd)] = alt
                prev[(rr,cc,ll,dd)] = (r,c,l,d)
            if k not in qelm:
                heappush(Q,(dist[k],k))
                qelm[k] = 1
    
minn,I,J = 1e5, -1,-1
for i in range(10):
    for j in range(4):
        if dist[(R-1,C-1,i,j)] < minn:
            minn = (dist[(R-1,C-1,i,j)])
            I,J = i,j
lastheat = heatmap[R-1] [C-1]
firstheat = heatmap[0][0]
print(minn+lastheat-firstheat)