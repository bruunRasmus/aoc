import sys
import copy
f = open(sys.argv[1],'r')

lava = [list(l.rstrip()) for l in f]
spaces = [i for i,l in enumerate(lava) if l == []]
spaces = [-1]+spaces + [len(lava)] 
ts = [lava[spaces[i]+1:spaces[i+1]] for i in range (len(spaces)-1)]

def differBy1(l1,l2):
    flag = 0
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            flag +=1
            idx = i
        if flag > 1:
            return [False,-1]
    if flag ==1:
        return [True,idx]
    else:
        return [False,-1]
        
def posSmuHor(t,Hor = True):
    retval = []
    for i in range (len(t)-1):
        for j in range(i+1,len(t)):
            d = differBy1(t[i],t[j])
            if d[0]:
                if  Hor:
                    retval.append([i,d[1]])
                else:
                    retval.append([d[1],i])
    return retval
def posSmuAll(t):
    return posSmuHor(t) + posSmuHor(list(zip(*t)),False) 

def opposite(c):
    if c == '#':
        return '.'
    else: 
        return '#'

def findHorSym(t,changes,part2 = False):
    if part2:
        syms = []
        for ch in changes:
            tCopy = copy.deepcopy(t)
            tCopy[ch[0]][ch[1]] = opposite(tCopy[ch[0]][ch[1]])
            for c in range (len(tCopy)-1):
                offset = 1
                flag = True
                while flag and tCopy[c-offset+1] == tCopy[c+offset] :
                    if c-offset <0 or c+offset+1 >= len(tCopy):
                        syms.append(c+1)
                        flag = False
                    offset +=1
        return syms + [0]
    else:
        for c in range (len(t)-1):
                offset = 1
                while t[c-offset+1] == t[c+offset]:
                    if c-offset <0 or c+offset+1 >= len(t):
                        return (c+1)
                    offset +=1
        return 0
        
 
def findAllSym(t):
    p = posSmuAll(t)
    trans = [list(x) for x in zip(*t)]
    ptrans = [[y,x] for x,y in p]
    hor = findHorSym(t,p,True)
    horOld = findHorSym(t,"_",False)
    ver  = findHorSym(trans,ptrans,True)
    verOld = findHorSym(trans,"_",False)
    if horOld != 0:
        while horOld in hor:
            hor.remove(horOld)
    if verOld != 0:
        while verOld in ver:
            ver.remove(verOld)
    return hor[0]*100 + ver[0]
print(sum([findAllSym(t) for t in ts]))     