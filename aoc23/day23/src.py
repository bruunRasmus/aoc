from collections import deque,defaultdict
lines = open("input.txt").read().strip().splitlines()
G = [list(l) for l in lines]
R,C = len(G),len(G[0])

paths = [(r,c) for r in range(R) for c in range(C) if G[r][c]!= "#"]
S,E = paths[0],paths[-1]

DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))
def find_neighbours(sr, sc):
    compressed = {}
    for dr, dc in DIRS:
        r, c = sr + dr, sc + dc
        if (r, c) not in paths:
            continue
        prev = (sr, sc)
        length = 1
        while True:
            next_cell = None
            degree = 0
            for dr, dc in DIRS:
                rr, cc = r + dr, c + dc
                if (rr, cc) in paths and (rr, cc) != prev:
                    degree += 1
                    next_cell = (rr, cc)
                    if degree > 1:
                        break
            if degree != 1:
                compressed[(r, c)] = length
                break
            prev = (r, c)
            r, c = next_cell
            length += 1
    return compressed

nbs = defaultdict(dict)
Q = deque([S])
while Q:
    u = Q.popleft()
    if u in nbs: continue
    nbs[u] = find_neighbours(*u)
    Q.extend(nbs[u])


best = -float("inf")
Q = deque([(0, S, {S})])

while Q:
    d, u, seen = Q.popleft()
    if u == E and d > best:
        best = d
    Q.extend((d + w, v, seen | {v}) for v, w in nbs[u].items() if v not in seen)

print(best)