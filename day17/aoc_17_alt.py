import sys
f = open(sys.argv[1],'r')
heatmap = f.read().strip().split('\n')
heatmap = [[int(c) for c in l ] for l in heatmap]

R= len(heatmap)
C = len(heatmap[0])

Q = set()
dist = {}
prev = {}
for indir in range(4):
    for l in range(3):
        for c in range(len(heatmap[0])):
            for r in range(len(heatmap)):
                key = (r,c,l,indir)
                Q.add(key)
                dist[key] = 1e10
                prev[key] = [-1,-1]
dist[(0,0,0,0)] = 0
dist[(0,0,0,1)] = 0
dist[(0,0,0,2)] = 0
dist[(0,0,0,3)] = 0
            
def neighbour(x,d,l):
    c,r = x
    ns =  [(c+1,r,1),(c-1,r,3),(c,r+1,0),(c,r-1,2)]
    ns = [(cc,rr,dd,(l+1)) if d==dd else (cc,rr,dd,0) for cc,rr,dd in ns]
    return ns

removed = set()

#print(Q)
while len(Q)>0:
    #print("1")
    #print(len(Q))
    #mval = 1e6
    mval = 1e10
    mq = -1
    #print(len(Q))
    for q in Q:
        if dist[q]<mval:
            mval = dist[q]
            mq = q
    #    if dist[q] < mval:
    #        mval = dist[q]
    #        mq = q
    #print(dist[mq])
    #print(mq)
    r,c,l,d = mq
    Q.remove(mq)
    removed.add(mq)
    if [r,c] == [len(heatmap)-1,len(heatmap[0])-1]:
        print("YeS")
        break
    
    for n in neighbour((c,r),d,l):
        cc,rr,dd,ll = n
        if 0<=cc<C and 0<=rr<R and ll < 3 and abs(dd-d)!=2:
            alt = dist[(r,c,l,d)] + heatmap[r][c]
            key = (rr,cc,ll,dd)
            if key not in removed:
                Q.add(key)
                if alt < dist[key]:
                    dist[key] = alt
                    prev[key] = (r,c,l,d)

             
minn = 1e5      
I = -1
J = -1
for i in range(3):
    for j in range(4):
        if dist[(len(heatmap)-1,len(heatmap[0])-1,i,j)] < minn:
            minn = (dist[(len(heatmap)-1,len(heatmap[0])-1,i,j)])
            I = i
            J = j
lastheat = heatmap[len(heatmap)-1] [len(heatmap[0])-1]
firstheat = heatmap[0][0]

print(minn+lastheat-firstheat)
#p = prev[(12,12,I,J)]
#print(p)
#while p!=(0,0,0,0):
#    print(p)
#    p = prev[p]
    




                    
        


