parts = open("input.txt",'r').read().strip().split("\n\n")

presents = []
regions = []
requirements = []

#parse
for p in parts:
    if "#" in p:
        present = p.split("\n")[1:]
        present_coords = []
        R,C = len(present),len(present[0])
        for r in range(R):
            for c in range(C):
                if list(present[r])[c] == "#":
                    present_coords.append((r,c))
        presents.append(present_coords)
    else:
        for l in p.split("\n"):
            size,req = l.split(": ")
            regions.append([int(x) for x in size.split("x")])
            requirements.append([int(x) for x in req.split()])

#symmetries
transforms=lambda x,y:[(x,y),(-y,x),( -x,-y),( y,-x),(x,-y),(-x,y),(y,x),(-y,-x)]
sym_presents = [
    list(zip(*[[(ttx + 1, tty + 1) for ttx, tty in transforms(x - 1, y - 1)] for x, y in present])) for present in presents
]

def is_valid(grid,r,c,present):
    R,C = len(grid),len(grid[0])
    for dr,dc in present:
        rr,cc = r+dr,c+dc
        if not(0<=rr<R and 0<=cc<C and grid[rr][cc] == "."):
            return False
    return True

def set_present(grid,r,c,present,char = "#"):
    for dr,dc in present:
        rr,cc = r+dr,c+dc
        grid[rr][cc] = char
    return grid

def solve(grid,req): #correct, but way too slow for even the unsatisfiable test input
    R,C = len(grid),len(grid[0])
    PRESENT_SIZE = sum(len(presents[i])*req[i] for i in range(len(req)))
    GRID_SIZE = R*C
    if GRID_SIZE<PRESENT_SIZE: #doing alot of heavy lifting
        return False
    if sum(req) == 0:
        return grid
    for r in range(R-2):
        for c in range(C-2):
            for i in range(len(req)):
                if req[i] > 0:
                    for s in sym_presents[i]:
                        if is_valid(grid,r,c,s):
                            grid = set_present(grid,r,c,s,char = str(i))
                            req[i]-=1
                            if solve(grid,req):
                                return grid
                            grid = set_present(grid,r,c,s,char=".")
                            req[i]+=1
    return False

ans1 = 0
for region,req in zip(regions,requirements):
    R,C = region
    grid = [["." for _ in range(R)] for _ in range(C)]
    if solve(grid,req): ans1 += 1
print(ans1)