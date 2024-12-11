import sys
with open(sys.argv[1],'r') as f:
    D = f.read().strip()
    stones = D.split()

dp = {}
def solve(s,t):
    if (s,t) in dp.keys():
        return dp[(s,t)]
    if t == 0:
        retval = 1
    elif s == '0':
        retval = solve('1',t-1)
    elif len(s) % 2 == 0:
        mid = len(s)//2
        retval = solve(str(int(s[:mid])),t-1)  + solve(str(int(s[mid:])),t-1) 
    else:
        retval = solve(str(int(s)*2024),t-1)
    
    dp[(s,t)] = retval
    return retval

s1,s2 = 0,0
for s in stones:
    s1+=solve(s,25)
    s2+=solve(s,75)
print(s1,s2)