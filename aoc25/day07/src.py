from collections import defaultdict
lines = open("input.txt",'r').read().strip().split("\n")
grid = [list(l) for l in lines]

R,C = len(grid),len(grid[0])

splitter = []

for r in range(R):
    for c in range(C):
        if grid[r][c] == "S": S = (r,c)
        if grid[r][c] == "^": splitter.append((r,c))

ans1 = 0
DP = defaultdict(int)

def solve(r,c):
    global ans1
    if (r,c) not in DP:
        if r == R:
            DP[(r,c)] = 0
        elif (r+1,c) in splitter:
            DP[(r,c)] = 1 + solve(r+1,c-1) + solve(r+1,c+1)
            ans1 +=1 #safe to update, since already encountered paths have updated the memo
        else:
            DP[(r,c)] = solve(r+1,c)
    return  DP[(r,c)]    

ans2= 1 + solve(*S)
print(ans1,ans2)