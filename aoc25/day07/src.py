from collections import defaultdict
lines = open("input.txt",'r').read().strip().split("\n")
grid = [list(l) for l in lines]

R,C = len(grid),len(grid[0])
ans1 = ans2 = 0
DP = defaultdict(int)

splitter =  [(r,c) for r in range(R) for c in range(C) if  grid[r][c] == "^"]
S =         [(r, c) for r in range(R) for c in range(C) if grid[r][c] == "S"][0]

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

ans2 += 1 + solve(*S)
print(ans1,ans2)