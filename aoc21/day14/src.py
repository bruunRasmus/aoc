from collections import defaultdict
temp, pair = open("input.txt").read().strip().split("\n\n")

insertion = {}
for p in pair.splitlines():
    pat,new = p.split(" -> ")
    c1,c2 = pat
    insertion[(c1,c2)] = new

def combine_dicts(d1,d2):
    new_d = defaultdict(int)
    for k in d1:
        new_d[k]+=d1[k]
    for k in d2:
        new_d[k]+=d2[k]
    return new_d

DP  = {}
def solve(c1,c2,t):
    if (c1,c2,t) not in DP:
        if t == 0:
            DP[(c1,c2,t)] = {c1:1}
        else:
            c3 = insertion[(c1,c2)]
            DP[(c1,c2,t)] = combine_dicts(solve(c1,c3,t-1),solve(c3,c2,t-1))
    return DP[(c1,c2,t)]
    
for T in [10,40]: 
    freq = {temp[-1]:1}
    for i in range(len(temp)-1):
        c1,c2 = temp[i],temp[i+1]
        freq = combine_dicts(freq,solve(c1,c2,T))
    print(max(freq.values())-min(freq.values()))