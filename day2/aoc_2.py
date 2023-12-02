import sys

def maxColors(lst):
    seen = {"red":0,"green":0,"blue":0}
    for combination in lst:
        cdict = stringToDict(combination)
        for k in cdict.keys():
            seen[k] = max(cdict[k],seen[k])
    return seen
        
def stringToDict(s):
    sep = s.rstrip().split(", ")
    kv  = list(map(lambda x: x.split(" "), sep))
    return {color:int(val) for val, color in kv}

f = open(sys.argv[1],"r")

def result(records)
    sum = 0
    for game in records:
        prod = 1
        _,record = game.split(": ")
        count = maxColors(record.split("; "))
        for v in count.values():
            prod *= v
        sum += prod
    return sum
            
print(result(f))
