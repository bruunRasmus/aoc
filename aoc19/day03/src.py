lines = open("input.txt").read().strip().splitlines()

ans1 = ans2 = 0
DIRS = {"R":(0,1),"L":(0,-1),"D":(1,0),"U":(-1,0),}
cross = []

for wire in lines:
    SEEN = {}
    x,y = 0,0
    TOTAL_STEPS = 0
    for a in wire.split(","):
        d,l =a[0],a[1:]
        for i in range(int(l)):
            TOTAL_STEPS += 1
            dx,dy = DIRS[d]
            x,y = x+dx,y+dy
            SEEN[(x,y)] = TOTAL_STEPS if (x,y) not in SEEN else SEEN[(x,y)]
    cross.append(SEEN)

C = ({pos:cross[0][pos] + cross[1][pos] for pos in cross[0] if pos in cross[1]})

ans1 = min(abs(x) + abs(y) for x,y in C)
ans2 = min(C.values())
        
print(ans1)
print(ans2)