lines = open("input.txt",'r').read().strip().split("\n")
coords = [tuple([int(x) for x in p.split(",")]) for p in lines]
coords = coords + [coords[0]]

ans1 = ans2 = 0
N = len(coords)

def intersects(points):
    (x1,y1),(x2,y2) ,(x3,y3),(x4,y4) = points
    if x1 == x2:
        vx = x1
        vymin, vymax = sorted([y1, y2])
        hy = y3
        hxmin, hxmax = sorted([x3, x4])
        return (hxmin <= vx <= hxmax) and (vymin  < hy < vymax)
    else:
        vx = x3
        vymin, vymax = sorted([y3, y4])
        hy = y1
        hxmin, hxmax = sorted([x1, x2])
        return (hxmin < vx < hxmax) and (vymin  <= hy <= vymax)

for i in range(N-1):
    for j in range(i+1,N):
        x1,y1 = coords[i]
        x2,y2 = coords[j]
        area = (abs(x2-x1)+1) * (abs(y2-y1)+1)
        ans1 = max(ans1,area)
        if area <= ans2: continue

        valid = True
        for p1,p2 in [((x1,y1),(x1,y2)),
                      ((x1,y1),(x2,y1)),
                      ((x2,y2),(x1,y2)),
                      ((x2,y2),(x2,y1))]:
            for k in range(N-1):
                p3 = coords[k]
                p4 = coords[k+1]
                points = (p1,p2,p3,p4)
                if intersects(points):
                    valid = False
                    break
            if not valid:
                break    
        else:
            ans2 = max(ans2,area)

print(ans1)
print(ans2)