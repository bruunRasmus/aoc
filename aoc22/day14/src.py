import sys
f = open(sys.argv[1],'r')

process = lambda lst:[[int(n) for n in coord.split(',')] for coord in  lst.rstrip().split(" -> ")]
coords = [process(line) for line in f]

env = {}
def allRocks(start,end):
    xS,yS = start
    xE,yE = end
    if xE > xS:
        return [(xS+i,yS) for i in range(xE-xS+1)]
    elif xS > xE:
        return [(xE+i,yE) for i in range(xS-xE+1)]
    if yE > yS:
        return [(xS,yS+i) for i in range(yE-yS+1)]
    elif yS > yE:
        return [(xE,yE+i) for i in range(yS-yE+1)]

for rocks in coords:
    for i in range(len(rocks)-1):
        for x,y in allRocks(rocks[i],rocks[i+1]):
            env[x,y] = 1

deepestRock = max([y for x,y in env.keys()])
for i in range(1000):
    env[i,deepestRock+2] = 1

def blocked(pos,env):
    x,y = pos
    return  (x,y) in env.keys()
       
flag = False
def fall(pos,env):
    global flag
    x,y = pos
    #if y > deepestRock:
    #    flag = True
    #    return 0
    if blocked((500,0),env):
        flag = True
        return 0

    if blocked((x,y+1),env):
        if blocked((x-1,y+1),env):
            if blocked((x+1,y+1),env):
                env[x,y] = 1
                return 1
            else:
                return fall((x+1,y+1),env)
        else:
            return fall((x-1,y+1),env)
    else:
        return fall((x,y+1),env)
i = 0      
while not flag:
    fall((500,0),env)
    i+=1
    
print(i-1)