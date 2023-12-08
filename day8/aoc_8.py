import sys
import numpy as  np

f = open(sys.argv[1],'r')

def rlToInt (rlstring):
    return [1 if (c == 'R') else 0 for c in rlstring]

def findPathLength(start,endFun):
    ends = [s for s in  d if endFun(s)]
    i,current = (0,start)
    while current not in ends:
        for walk in rl:
            current = d[current][walk]
            i+=1
    return i

rl = rlToInt(f.readline().rstrip()) #Left/Right string
d = {l[:3]:[l.split("(")[1][:3],l[-5:-2]] for l in f if l[0]!= '\n'} #Dict of edges

#Part 1
print(findPathLength('AAA',lambda s:s=='ZZZ')) #Walk from AAA to ZZZ

#Part 2
currentMany  = [k for k in d if k[2]=='A'] #Walks from **A to **Z
#Walks |s1->z1| = n, |s2->z2|= m => lcm(n,m) is |walk| from both s1->z1 and s2->z2,
#if any walk from z1 cycles back to z1 in n steps, likewise for z2. So input is special case
print(np.lcm.reduce(([findPathLength(c,lambda s: s[2]=='Z') for c in currentMany]))) 


       