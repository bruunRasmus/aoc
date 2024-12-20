import sys
from collections import defaultdict
sys.setrecursionlimit(10**8)
with open(sys.argv[1],'r') as f:
    D = f.read().strip()
    tw,patterns = D.split('\n\n')
    tw = tw.split(', ')
    patterns = patterns.split('\n')

DP  = defaultdict(int)
DP[''] = 1

def solve(pattern):
    if pattern in DP:
        retval =  DP[pattern]
    else:
        retval = sum((pattern[:i] in tw) * solve(pattern[i:]) for i in range(1,len(pattern)+1))
        DP[pattern] = retval
    return retval

s1,s2=0,0
for t in tw:
    DP[t] = solve(t)
for p in patterns:
    v = solve(p)
    s1+= v>0
    s2 += v
    
print(s1,s2)