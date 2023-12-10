import sys
f = open(sys.argv[1],'r')

def mapping (c):
    match c:
        case 'S': return ('start','start')
        case '|': return ('south','north')
        case '-': return ('west','east')
        case 'L': return ('north','east')
        case 'J': return ('west','north')
        case '7': return ('west','south')
        case 'F': return ('south','east')
        case _ :  return (None,None)

def opposite(dir):
    match dir:
        case 'south': return 'north'
        case 'north': return 'south'
        case 'west':  return 'east'
        case 'east':  return 'west'
    

def findS(l):
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] ==  ('start','start'):
                return [j,i]

def next(inDirection,position):
    x,y = position
    match inDirection:
        case 'south': position =  [x,y+1]
        case 'north': position =  [x,y-1]
        case 'west':  position =  [x-1,y]
        case 'east':  position =  [x+1,y]
    newDirections = idx(position,land)
    if opposite(inDirection
                ) in newDirections:
        frm = newDirections.index(opposite(inDirection))
        outDirection = newDirections[abs(1-frm)]
    else:
        outDirection = None
    return [inDirection,outDirection,position]
    
    

land = [[mapping(c) for c in line.rstrip()] for line in f]
def idx(pair,l):
    i,j = pair
    return l[j][i]

s = findS(land)
def closedLoop(pos,direction):
    start = pos
    visited = []
    while direction != None:
        inDirection,direction,pos = next(direction,pos)
        
        if direction == 'north':
            if inDirection in ['north']:
                visited.append([pos,'up'])
            else:
                visited.append([pos,'horizontal'])
                
        elif direction == 'south':
            if inDirection in ['west','east','south']:
                visited.append([pos,'down'])
            else:
                visited.append([pos,'horizontal'])
                
        elif direction == 'west':
            if inDirection in ['north']:
                visited.append([pos,'up'])
            else:
                visited.append([pos,'horizontal'])
                
        elif direction == 'east':
            if inDirection in ['north']:
                visited.append([pos,'up'])
            else:
                visited.append([pos,'horizontal']) 
                 
        elif inDirection == 'north':
            visited.append([pos,'up'])     
        if pos == start:
            return [visited,len(visited)/2]
    return [None,None]

loops = [closedLoop(s,firstDir) for firstDir in ['east','west','north','south']]

maxLoop = 0
maxIdx = 0
for i,l in enumerate(loops):
    if l[1]!= None and l[1]>maxLoop:
        maxLoop = l[1]
        maxIdx = i

loopValue = loops[maxIdx][0]
loopValueCoords = [l[0] for l in loopValue]

s=0
for i in range(len(land)):
    loopChars =  [l[0] for l in loopValue if (l[0][1]==i) and l[1]!='horizontal']
    inside = False
    for j,c in enumerate(land[i]):
        if [j,i] not in loopValueCoords and inside == True:
            s+=1
        if [j,i] in loopChars:
            inside = not inside
       
print(s)
            
        
        
        
    
