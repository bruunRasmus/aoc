import sys
def seedRangeToList(s):
    lst = stringToList(s)
    return [[lst[i],lst[i+1]] for i in range(0,len(lst),2)]

def stringToList(s):
    return list(map(lambda x: int(x),s.split(" ")))

def intersection(s1,l1,s2,l2): # return start and length of interval
    e1 = s1+l1
    e2 = s2+l2
    if s2>e1 or s1>e2:
        return None
    else:
        s3 = max(s1,s2)
        e3 = min(e1,e2)
        return [s3,e3-s3]

def result(file):
    f = open(file,'r')
    for line in f:
        if line[:6] == "seeds:":
            keys = seedRangeToList(line[7:].rstrip())
        elif line[0].isalpha():
            changed = []
        elif line[0].isnumeric():
            for i,k in enumerate(keys):
                destinationRange,sourceRange,rangeLength = stringToList(line.rstrip())
                inter = intersection(
                        k[0],k[1],sourceRange,
                        rangeLength)
                if inter!= None and i not in changed:
                    if inter[1]>0:
                        if inter[0]-k[0] > 0:
                            keys.append([k[0],inter[0]-k[0]]) #before intersection
                        if k[0]+k[1]-inter[0]-inter[1]> 0 :
                            keys.append([inter[0]+inter[1],k[0]+k[1]-inter[0]-inter[1]]) #after intersection
                        if inter[1] > 0:
                            print(inter[0]-sourceRange)
                            keys[i] = [inter[0]-sourceRange + destinationRange,inter[1]]
                        changed.append(i)                 
    return min([k[0] for k in keys])

print(result(sys.argv[1]))

            
            
