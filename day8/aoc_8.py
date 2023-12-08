import sys
import numpy as  np

f = open(sys.argv[1],'r')

def rlToInt (rlstring):
    return [1 if (c == 'R') else 0 for c in rlstring]

rl = rlToInt(f.readlines(2)[0].rstrip())
d = {}
for l in f:
    if l[0]!= '\n':
        d[l[:3]] = [l.split("(")[1][:3],l[-5:-2]]
#Part 1
current = 'AAA'
i = 0
while current != 'ZZZ':
    for walk in rl:
        if current != 'ZZZ':
            current = d[current][walk]
            i+=1
        else:
            break
print(i)
currentMany  = [k for k in d if k[2]=='A']
# Part 2
def loopCountAndZs(start): 
    zs = []
    i = 0
    current = start
    flag = True
    while flag:
        for walk in rl:
            #print(current)
            current = d[current][walk]
            i+=1
            if current[2] == 'Z':
                if current in [z[1] for z in zs]:
                    flag = False
                else:
                    zs.append([i,current])
            if current == start:
                flag = False
                break
    return (zs[0][0]) #they never visit more than 1 z before looping

z = [loopCountAndZs(c) for c in currentMany]
print(np.lcm.reduce(z))
       