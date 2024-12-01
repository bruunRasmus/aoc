import sys
f = open(sys.argv[1],'r')


s = 'Sensor at x=2, y=18: closest beacon is at x=-2, y=15'

process = lambda lst: [int("".join(numChar)) 
                       for numChar in [[c for c in s if c.isdigit() or c =='-'] 
                            for s  in lst.rstrip().split('=')[1:] ]]


coords = [(process(line)[:2], process(line)[2:]) for line in f]


def mDist(S,B):
    xS,yS = S
    xB,yB = B
    return(abs(xS-xB) + abs(yS-yB))

Y = 2000000
noBeacon = set([])
balls = []

def noBeaconAtY(S,B,y):
    #global noBeacon
    #xS,yS = S
    global balls
    dB = mDist(S,B)
    #dY = mDist(S,(xS,y))
    balls.append((S,dB))
    #print(f'manhatten dist between {S} and {B} is {d}')
    #for i in range(dB-dY+1):
    #    noBeacon.add(xS-i)
    #    noBeacon.add(xS+i)
        #print(f'added {xS+i} and {xS-i}' )
for c in coords:
    S,B = c
    #print(S,B)
    noBeaconAtY(S,B,Y)

for c in coords:
    (xS,yS),(xB,yB) = c
    if yS == Y and xS in noBeacon:
        noBeacon.remove(xS)
    if yB == Y and xB in noBeacon:
        noBeacon.remove(xB)

V = 20

def getBoundingDiamond(S,r):
    BD = []
    x,y = S
    for i in range(r+2):
        BD.append((x+r-i+1,y-i))
        BD.append((x-(r-i+1),y-i)) 

    return BD

candidates =  [c for l in [getBoundingDiamond(s,r) for s,r in balls] for c in l]
print(len(set([c for c in candidates if candidates.count(c) > 1])))

#print(noBeacon)
#print(len(noBeacon))