import sys
f = open(sys.argv[1],'r')

mirrors = f.read().split('\n')[:-1]

def newPos(c,r,dir):
    match dir:
        case 'right':
            return (c+1,r)
        case 'left':
            return (c-1,r)
        case 'up':
            return (c,r-1)
        case 'down':
            return (c,r+1)

def newDir (oldDir,mir):
    match mir:
        case '.':
            return [oldDir]
        case '|':
            if oldDir in ['right','left'] :
                return ['up','down']
            else:
                return [oldDir]
        case '-':
            if oldDir in ['up','down'] :
                return ['right','left']
            else:
                return [oldDir]
        case '/':
            match oldDir:
                case 'down':
                    return ['left']
                case 'right':
                    return ['up']
                case 'left':
                    return ['down']
                case 'up':
                    return ['right']
        case '\\':
            match oldDir:
                case 'down':
                    return ['right']
                case 'right':
                    return ['down']
                case 'left':
                    return ['up']
                case 'up':
                    return ['left']


sys.setrecursionlimit(5000)
def beam (c,r,dir):
    dnew = newDir(dir,mirrors[r][c])
    for dd in dnew:
        try:
            if dd in vdir[c,r]:
                return
            else:
                vdir[c,r] = vdir[c,r].append(dd)
        except:
            vdir[c,r] = dd
            
        cnew,rnew = newPos(c,r,dd)
        if (0<=cnew<len(mirrors[0])) and (0<=rnew<len(mirrors)):
            beam(cnew,rnew,dd)

best = 0
for start in range(len(mirrors)):
    vdir = {}    
    beam(0,start,'right')
    best = max(best,len(vdir))
    
    vdir = {} 
    beam(0,len(mirrors)-start-1,'left')
    best = max(best,len(vdir))    
for start in range(len(mirrors)):
    vdir = {}
    beam(start,0,'down')
    best = max(best,len(vdir))
    
    vdir = {}
    beam(len(mirrors)-1-start,0,'up')
    best = max(best,len(vdir))

print(best)