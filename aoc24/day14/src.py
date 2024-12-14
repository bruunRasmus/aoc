import sys
with open(sys.argv[1],'r') as f:
    D = f.read().strip()
    lines = D.split('\n')

robots = []
for l in lines:
    p,v = l.split()
    _,numsP = p.split('=')
    px,py = numsP.split(',')

    _,numsV = v.split('=')
    vx,vy = numsV.split(',')

    robots.append([[int(px),int(py)],(int(vx),int(vy))])

R,C = (103,101) if sys.argv[1] == '.\input.txt' else (7,11)
p,v = zip(*robots)
p = list(p)

def show_grid(grid):
    for r in range(R):
        for c in range(C):
            if [c,r] in grid:
                print('#',end = '')
            else:
                print(' ',end = '')
        print('')

def avg_dist(points):
    n = len(points)
    return sum(abs(ax - bx) + abs(ay - by) 
               for ax, ay in points 
               for bx, by in points) / (n**2)

for i in range(1,10000):
    for j in range(len(robots)):
        px,py = p[j] 
        vx,vy = v[j]
    
        px = (px + vx) % C
        py = (py + vy) % R
        p[j] = [px,py]

    if avg_dist(p)<45: #robots are close together when forming the tree
        print('part2:',i)
        show_grid(p)
        break

    if i == 100:
        s = [0, 0, 0, 0]
        for px, py in p:
            if px != C // 2 and py != R // 2: 
                quadrant = (px > C // 2) * 2 + (py > R // 2)
                s[quadrant] += 1
        pr = 1
        for f in s:
            pr*= f
        print('part1:',pr)