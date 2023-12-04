import sys
import re

def numberOfMatches(tup):
    xs,ys = tup
    sum = 0
    for x in xs:
        for y in ys:
            if x==y:
                sum += 1
    return sum
    #if sum > 0:
    #    return 2**(sum-1)
    #else:
    #    return 0

def removeEmptyFirst(lst):
    if lst[0] == '':
        return lst[1:]
    else: 
        return lst

def inputToLists(s):
    nums = s.split(": ")[1].split(" | ")
    xs,ys = list(map(lambda x: removeEmptyFirst(re.split("\s\s|\s",x)),nums))
    return (xs,ys)

def add1(d,i):
    if i in d:
        d[i]+=1
    else:
        d[i] = 1

def result(f):
    idx = 1 
    won = {1:1}
    for line in f:
        add1(won,idx+1)
        if not idx in won:
            break
        points = numberOfMatches(inputToLists(line.rstrip()))
        for i in range(1,points+1):
            if idx + i in won:
                won[idx+i] += won[idx]
            else:
                won[idx+i] = won[idx]
        idx += 1
    wonCount = [won[k] for k in range(1,idx)]
    print(wonCount)
    return sum(wonCount)

file = open(sys.argv[1],'r')
print(result(file))