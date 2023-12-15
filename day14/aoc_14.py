import sys
import time
f = open(sys.argv[1],'r')

lines = [s.rstrip() for s in f]

def rotate(llist):
    l=  [list(i) for i in (zip(*llist))]
    for lst in l:
        lst.reverse()
    return l

def tilt(lst):
    current = 0
    for i,c in enumerate(lst):
        if c=='O':
            current += 1
            lst[i]='.'
        if c == '#':
            lst[i-current:i] = ['O']*(current)
            current = 0
    if current > 0:
        lst[-current:] = ['O']*current
    return lst

rocks = lines
T =  1000000000
ss = []
config = []
l = len(rocks)

for t in range(T):
    for i in range (4):
        rocks = rotate(rocks)
        rocks = [tilt(s) for s in(rocks)]
    s = 0
    co = []
    for i,r in enumerate(rocks):
        for j,c in enumerate(r): 
            if (c=='O'):
                s += (l-i)
                co.append([i,j])
    
    if co in config:
        print("duplicate found at t= ", t, "last seen at: ", config.index(co))
        print("so value at T= 1000000000 is SS at index: 1000000000-",t,"%",t-config.index(co), "-1 =",
               ss[(1000000000-t) % (t-config.index(co))+config.index(co)-1])
        break
    ss.append(s)
    config.append(co)
   
