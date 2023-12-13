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
    key = (k,i,j)
    
    print(records)

    if len(records) == i:
        #print("yes")
        #print(int(valid(records,ints)))
        #print(records,ints)
        states[key] = int(valid(records,ints))
        #print("returning with value: ",int(valid(records,ints)) )
        return int(valid(records,ints))
    
    match records[i]: 
        case '#':
            current +=1
            i       +=1
            #print("hashtag")
            return posConfig(k,records,ints,current,j,i)
        case '.':
            if current > 0:
                j       +=1
                current = 0
            i       +=1
            #print("dot")
            return posConfig(k,records,ints,current,j,i)
            
        case '?':
            if key in list(states.keys()):
                #print("no way")
                return states[key]
            else:
                print(states)
                v1 = posConfig(k,records[:i]+'#'+records[i+1:],ints,current,j,i+1)
                #print("v1",v1)
                v2 = posConfig(k,records[:i]+'.'+records[i+1:],ints,current,j,i+1)
                #print("v2",v2)
                
                states[key] = v1 + v2
                return states[key]
        case _:
            print("no")
            return 0
    

sum = 0
for k,line in enumerate(f):
    records,ints = line.split()
    records = ((records + '?')*5)[:-1]
    ints = [int(i) for i in ints.split(',')]*5
    sum += posConfig(k,records, ints,0,0,0)
    
print(sum)

    