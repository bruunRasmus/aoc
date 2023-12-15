import sys
import time
f = open(sys.argv[1],'r')

rocks = [s.rstrip() for s in f]

def rotate(llist):
    return [list(i)[::-1] for i in (zip(*llist))]

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

ss = []
config = []

for t in range(1000000000):
    for i in range (4):
        rocks = [tilt(s) for s in rotate(rocks)]
    s = 0
    co = []
    for i,r in enumerate(rocks):
        for j,c in enumerate(r): 
            if (c=='O'):
                s += (len(rocks)-i)
                co.append([i,j])
    if co in config:
        print("duplicate found at t =", t, "last seen at: ", config.index(co))
        print("so value at T= 1e9 is SS at index: (1e9 -",t,") % (",t-config.index(co), ") - 1 =",
               ss[(1000000000-t) % (t-config.index(co))+config.index(co)-1])
        break
    ss.append(s)
    config.append(co)