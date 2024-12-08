import sys

order = {}
updates = []
with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.rstrip()
        if '|' in line:
            a, b = map(int, line.split('|'))
            order.setdefault(a, []).append(b)
        elif len(line) > 1:
            updates.append([int(x) for x in line.split(',')])

def qs(lst):
    if not lst or all(elm not in order for elm in lst):
        return lst
    
    pivot = next((elm for elm in lst if elm in order), lst[0])
    
    ls,gr = [],[]
    for elm in lst:
        if elm in order[pivot]:
            gr.append(elm)
        elif elm != pivot:
            ls.append(elm)
    
    return qs(ls)+[pivot]+qs(gr)

s1 = s2 = 0
for row in updates:
    flag = True
    n = len(row)
    for i in range(n):
        a = row[n-i-1]
        for j in range(n-i):
            b = row[n-i-j-1]
            if a in order.keys() and b in order[a]:
                flag = False; break
    if flag:
        s1+=row[n//2]
    else:
        s2 += qs(row)[n//2]
        
print(s1)
print(s2)