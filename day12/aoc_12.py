import sys
f = open(sys.argv[1],'r')

def valid(records,ints):
    current = 0
    matching = []
    for c in records:
        if c=='#':
            current += 1
        elif c == ".":
            if current>0:
                matching.append(current)
                current = 0
    if current > 0:
        matching.append(current)  
    return matching == ints

states = {}

def posConfig(k,records,ints,current, j,i):
    key = (k,j,i,current)
    if key in states:
        return states[key]
    if len(records) == i:
        return int(valid(records,ints))
    s = 0
    match records[i]: 
        case '#':
            s+= posConfig(k,records,ints,current+1,j,i+1)
        case '.':
            if current > 0 and j<len(ints) and ints[j] == current:
                s+=  posConfig(k,records,ints,0,j+1,i+1)
            elif current == 0:
                s += posConfig(k, records,ints,0,j,i+1)
        case '?':
            v1 = posConfig(k,records[:i]+'#'+records[i+1:],ints,current+1,j,i+1)
            if current > 0 and j<len(ints) and ints[j] == current:
                v2 =  posConfig(k,records[:i]+'.'+records[i+1:],ints,0,j+1,i+1)
            elif current == 0:
                v2 = posConfig(k, records[:i]+'.'+records[i+1:],ints,0,j,i+1)
            else: 
                v2 = 0
            s+= (v1 + v2)
    states[key] = s
    return s
    
sum = 0
for k,line in enumerate(f):
    records,ints = line.split()
    records = ((records + '?')*5)[:-1]
    ints = [int(i) for i in ints.split(',')]*5
    sum += posConfig(k,records, ints,0,0,0)  
print(sum)  