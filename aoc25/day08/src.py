from math import sqrt,prod

lines = open("input.txt",'r').read().strip().split("\n")
points = [[int(x) for x in l.split(",")] for l in lines]
P = len(points)

dists = []
for i,(x1,y1,z1) in enumerate(points):
    for j,(x2,y2,z2) in enumerate(points):
        if i<j:
            d = sqrt((x1-x2)**2 +(y1-y2)**2+(z1-z2)**2 )
            dists.append((d,(i,j)))
dists.sort()

componenets =[[i] for i in range(P)]
for i,(d,(p1,p2)) in enumerate(dists): 
    for k in range(len(componenets)):
        if p1 in componenets[k]: g1 = k
        if p2 in componenets[k]: g2 = k
    if g1 != g2:
        componenets[g1].extend(componenets[g2])
        del  componenets[g2]

    if i == 999:
        ans1 = prod(sorted([len(c) for c in componenets])[-3:])
    if len(componenets) == 1:
        ans2 = points[p1][0]*points[p2][0]
        break

print(ans1,ans2)