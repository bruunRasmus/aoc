from collections import defaultdict
temp, pair = open("test.txt").read().strip().split("\n\n")

replacements = {}
for p in pair.splitlines():
    pat,new = p.split(" -> ")
    replacements[pat] = pat[0] + new
 

def combine_dicts(a,b):
    for k in a:
        if k in b:
            b[k]+=a[k]
        else:
            b[k]=a[k]
    return b
 
DP = defaultdict(dict)   
def solve(pair,n):
    if (pair,n) not in DP:
        if n == 0:
            v = defaultdict(int)
            for p in pair:
                v[p]+= 1
            DP[(pair,n)] = v
        elif pair in replacements:
            p1 = replacements[pair]
            p2 = p1[1]+ pair[1]
            cd = combine_dicts(solve(p1,n-1), solve(p2,n-1))
            cd[p1[1]] -= 1
            DP[(pair,n)] = cd
        else:
            DP[(pair,n)] = solve((pair),n-1)
    return DP[(pair,n)]
 
ans1 = 0
freq = defaultdict(int)

for i in range(len(temp)-1):
    s = solve(temp[i:i+2],10)
    print(s)
    for c in s:
        freq[c] += s[c]

ans1 = max(freq.values()) - min(freq.values())    
print(ans1)

N = 10
for _ in range(N):
    new_temp = ""
    for i in range(len(temp)-1):
        window = temp[i:i+2]
        if window in replacements:
            new_temp += replacements[window]
        else:
            new_temp += window[0]
    new_temp += temp[-1]
    temp = new_temp

freq = defaultdict(int)
for c in temp:
    freq[c]+=1

ans1 = max(freq.values()) - min(freq.values())    
print(ans1)
