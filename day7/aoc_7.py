import sys

def handToLabel(hand):
    d = {k:0 for k in hand}
    for k in hand:
        if k != 'J':
            d[k] += 1
            
    d[max(d, key=d.get)] += hand.count('J')
    
    match max(d.values()):
        case 5: return 7
        case 4: return 6
        case 3:
            if sorted(d.values())[-2] == 2: return 5
            else: return 4
        case 2:
            if sorted(d.values())[-2] == 2: return 3
            else: return 2
        case 1: return 1
   
def sortKey(lhmlst):
    l,h,m = lhmlst
    newH = []
    for c in h:
        match c:
            case 'A': 
                newH.append(14)
            case 'K': 
                newH.append(13)
            case 'Q': 
                newH.append(12)
            case 'J': 
                newH.append(0)
            case 'T': 
                newH.append(10)
            case _:
                newH.append(int(c))
    return [l] + newH

def results(file):
    f = open(file,'r')
    order = []
    for line in f:
        h,m = line.split()
        order.append([handToLabel(h),h,m])
    order = sorted(order,key = sortKey)
    sum = 0
    for i,lhm in enumerate(order):
        sum += int(lhm[2])*(i+1)
    return sum

print(results(sys.argv[1]))