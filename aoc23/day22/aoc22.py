import sys
f = open(sys.argv[1],'r')

bricks = [tuple([tuple([int(x) for x in c.split(',')]) for c in tuple(l.rstrip().split('~'))]) for l in f]
bricks = [(b,i) for i,b in enumerate(bricks)]

zbricks = sorted(bricks,key = lambda x: min(x[0][0][2],x[0][1][2]))
settled = []

# Return true if line segments AB and CD intersect
def intersect(A,B,C,D):
    (ax,ay) = A
    (bx,by) = B
    (cx,cy) = C
    (dx,dy) = D    
    if not (max(ay,by)< min(cy,dy) or max(cy,dy) <min(ay,by)): #y intersects
        if not (max(ax,bx)< min(cx,dx) or max(cx,dx) <min(ax,bx)): #x intersects
            return True
    return False

carriedBy = {z:set() for z in zbricks}
carries = {z:set() for z in zbricks}

def fall(b): #very slow, why?
    bb, nameb = b
    [x1,y1,z1],[x2,y2,z2] = bb
    minz = min(z1,z2)
    flag = False
    for i in range(minz):
        for c in settled:
            cc,namec = c
            [cx1,cy1,cz1old,cz1],[cx2,cy2,cz2old,cz2] = cc
            if minz - i in [cz1,cz2]:
                if intersect((x1,y1),(x2,y2),(cx1,cy1),(cx2,cy2)):
                    carriedBy[b].add(c)
                    carries[(((cx1,cy1,cz1old),
                              (cx2,cy2,cz2old)),
                               namec)].add(b)
                    if not flag:
                        settled.append(((((x1,y1,z1,(z1-(i-1))),
                                          (x2,y2,z2,(z2-(i-1))))),
                                           nameb))
                    flag = True
        if flag:
            return
    settled.append(((((x1,y1,z1,(1)),
                      (x2,y2,z2,(1)))),
                       nameb))
    return

for b in zbricks:
    fall(b)

def disintegrate(bs,all):
    retval = set()
    if len(bs) == 0: 
        return 0
    for b in bs:#bs disintegrated in previous iteration
        for c in carries[b]:
            cbi = set([x[1] for x in carriedBy[c]]) #brick carrying c
            if cbi.issubset(all) and c[1] not in all:#if all bricks carrying c have been disintegrated
                retval.add(c)                       #c is also disintegrated
                all.add(c[1])                       
    return len(retval) + disintegrate(retval,all)


print(sum([disintegrate(set([b]),set([b[1]])) for b in zbricks]))

removable = set()
for c in carries:
    flag = True
    for cb in carries[c]:
        if len(carriedBy[cb])==1:
            flag = False
    if flag:
        removable.add(c)
print(len(removable))    