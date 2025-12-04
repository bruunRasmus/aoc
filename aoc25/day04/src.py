from collections import deque

with open("input.txt", 'r') as f:
    grid = [list(line) for line in f.read().strip().split('\n')]

R,C = len(grid),len(grid[0])
N = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

ans1 = ans2 = 0
Q = deque()

#part1 + init Q with eligble removals only
for r in range(R):
    for c in range(C):
        if grid[r][c] == "@":
            s = sum(1 for rr,cc in N if 0<= r+rr < R and 0 <= c+cc <C and grid[r+rr][c+cc] == "@")
            if s<4:
                ans1 += 1
                Q.append((r,c))

#part2, maintain Q with affected cells
while Q:
    r,c = Q.popleft()
    ns = [(r+rr,c+cc) for (rr,cc) in N if 0<= r+rr < R and 0 <= c+cc <C and grid[r+rr][c+cc] == "@"]
    if len(ns)<4 and grid[r][c]=="@":
        grid[r][c] = "."
        ans2+=1
        Q.extend(ns)

print(ans1)
print(ans2)