from collections import deque

lines = open("input.txt",'r').read().strip()
lines = lines.split("\n")
grid = [list(l) for l in lines]

C,R = len(grid[0]),len(grid)
N = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

ans1 = ans2 = 0
Q = deque()

#part1 + init Q with eligble removals only
for r in range(R):
    for c in range(C):
        if grid[r][c] == "@":
            s = 0
            for rr,cc in N:
                if 0<= r+rr < R and 0 <= c+cc <C and grid[r+rr][c+cc] == "@": 
                    s+=1
            if s<4:
                ans1 += 1
                Q.append((r,c))

#part2, maintain Q with affected cells
while Q:
    r,c = Q.popleft()
    ns =[]
    for rr,cc in N:
        if 0<= r+rr < R and 0 <= c+cc <C and grid[r+rr][c+cc] == "@": 
            ns.append((r+rr,c+cc))
    if len(ns)<4 and grid[r][c]=="@":
        grid[r][c] = "."
        ans2+=1
        Q.extend(ns)

print(ans1)
print(ans2)