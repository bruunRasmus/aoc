import sys
f = open(sys.argv[1],'r')
    
def posConfig(records, ints,i):
    if len(records) == i:
        return int(valid(records,ints))
    if records[i] == '?':
        return posConfig(records[:i]+'#'+records[i+1:],ints,i+1) + posConfig(records[:i]+'.'+records[i+1:],ints,i+1)
    else:
        return posConfig(records,ints,i+1)
    
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


sum = 0
for line in f:
    records,ints = line.split()
    records = ((records + '?')*5)[:-1]
    ints = [int(i) for i in ints.split(',')]*5
    sum += posConfig(records, ints,0)

print(sum)
    

