from functools import cache

rules = open("input.txt").read().strip().splitlines()
nbs = {}

for r in rules:
    V,ns = r.split(" bags contain ")
    ns = ns.split(", ")
    nbs[V] = {}
    for n in ns:
        n = n.split(" ")
        color = " ".join(n[1:3])
        count = n[0]
        if count != "no" :
            nbs[V][color] = int(count)

@cache
def solve(v,sink = "shiny gold"):
    if v == sink:
        return True
    else:
        return any(solve(n) for n in nbs[v])

@cache
def solve2(v):
    s = 0
    for n in nbs[v]:
        s+= nbs[v][n] + nbs[v][n]*solve2(n)
    return s
    
ans1 = sum(solve(v) for v in nbs)-1
ans2 = solve2("shiny gold")
   
print(ans1)
print(ans2)