import sys
from math import prod
f = open(sys.argv[1],'r')
def sToDict (s):
    try:
        cond,next = s.split(':')
        v = cond[0]
        c = cond[1]
        n = cond[2:]
        return  (v,c,int(n),next)
    except:
        return s

xams,cases = f.read().split('\n\n')
xams = [x.split('{') for x in (xams.split('\n'))]
xams = {k:v.rstrip()[:-1].split(',') for k,v in xams}
xams = {k:[sToDict(s) for s in xams[k]]  for k in xams}

cases = [x[1:-1].split(',') for x in cases.split('\n')[:-1]]
ccc = []
for c in cases:
    d = {}
    for v in c:
        ch,n = v.split('=')
        d[ch] = [int(n),int(n)]
    ccc.append(d)

def part2(vals,idf):
    for cond in xams[idf]:
        ch = cond[0]
        if '<' in cond or '>' in cond:
            if cond[1] == '<':
                if vals[ch][1] < cond[2]: #interval falls entirely within boundary
                    if cond[3] == 'A':
                        return prod( [u-l+1 for l,u in vals.values()])
                    elif cond[3] != 'R':
                        return part2(vals,cond[3])
                    else:
                        return 0
                elif vals[ch][0]<cond[2]:# interval overlaps with boundary
                    newVal1 = {k:vals[k] for k in vals}
                    newVal1[ch] = [vals[ch][0],cond[2]-1]

                    newVal2 = {k:vals[k] for k in vals}
                    newVal2[ch] = [cond[2],vals[ch][1]]
                    return part2(newVal1,idf) + part2(newVal2,idf) # iterate again with split values
                else:
                    pass #gg go next
            elif cond[1] == '>':
                if vals[ch][0] > cond[2]: #interval falls entirely within boundary
                    if cond[3] == 'A':
                        return prod([u-l+1 for l,u in vals.values()])
                    elif cond[3] != 'R':
                        return part2(vals,cond[3])
                    else:
                        return 0
                elif vals[ch][1]>cond[2]:# interval overlaps with boundary
                    newVal1 = {k:vals[k] for k in vals}
                    newVal1[ch] = [vals[ch][0],cond[2]]

                    newVal2 = {k:vals[k] for k in vals}
                    newVal2[ch] = [cond[2]+1,vals[ch][1]]
                    return part2(newVal1,idf) + part2(newVal2,idf) # iterate again with split values
                else:
                    pass
        elif cond == 'R':
            return 0
        elif cond == 'A':
            return prod([u-l+1 for l,u in vals.values()])
        else:
            return part2(vals,cond)

All = {'x':[1,4000], 'm':[1,4000],'a':[1,4000],'s':[1,4000]}
s = 0
for c in ccc:
    s+=part2(c,'in')*sum([x for x,_ in c.values()])
print("part1:",s)
print("part2:",part2(All,'in'))
