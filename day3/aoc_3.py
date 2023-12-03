import numpy as np
import sys
from collections import ChainMap
from itertools import chain

def findSymbols(s):
    indices = []
    for i,c in enumerate(s):
        #if c!='.' and not(c.isdigit()):
        if c=='*':
            indices.append(i)
    return indices

def firstCharNumber(s):
    try:
        if s[0].isdigit():
            return True
    except: #index error
        return False

def findNumbers(s): #yikes
    i = 0
    indexNumberDict = {}
    while i < len(s):
        building = True
        currentNumber = ''
        j=0
        while building:
            if firstCharNumber(s[i+j:]):
                currentNumber += s[i+j]
                j+=1
            else: 
                building = False
        if currentNumber != '':
            indexNumberDict.update({k:(currentNumber,i) for k in range(i,i+j)})
        i+=j+1
    return indexNumberDict
 
def euclDist(x,y):
    m = np.array(x)-np.array(y)
    if np.linalg.norm(m)<=1.5: #sqrt(2)
        return True


def result (file):
    f = open(file,"r")
    retval = []
    sum = 0
    sym = [[(i,idx) for idx in findSymbols(line.rstrip())] for i,line in enumerate(f)]
    sym = list(chain.from_iterable(sym))
    f.close()
    f = open(file,"r")
    num = [{(i,k):v for k,v in findNumbers(line.rstrip()).items()} for i,line in enumerate(f)]
    num = dict(ChainMap(*num))
    for s in sym:
        gears = []
        for n in num:
            if euclDist(s,n):
                if not((num[n]) in gears):
                    gears.append(num[n])
        if len(gears)==2:
            sum+= int(gears[0][0])*int(gears[1][0])
    #return sum([int(l[0]) for l in retval])
    return sum

print(result(sys.argv[1]))
