import sys
f = open(sys.argv[1],'r')
input= [s for s in  f.readline().split("\n")[0].split(',')]

def HASH(s):
    currentValue = 0
    for c in s:
        currentValue += ord(c)
        currentValue*= 17
        currentValue %= 256
    return currentValue

boxes = [[] for _ in range(256)]

for s in input:
    if '-' in s:
        for elm in boxes[HASH(s[:-1])]:
            if s[:-1] == elm[0]:
                 boxes[HASH(s[:-1])].remove(elm)
                 break
    else:
        label,val  = s.split("=")
        flag = False
        for elm in boxes[HASH(label)]:
            if elm[0] == label:
                elm[1] = val
                flag = True
        if not flag:
            boxes[HASH(label)].append([label,val])

s = 0
for i, b in enumerate(boxes):
    for j,elm in enumerate(b):
        s+= (i+1)*(j+1)*int(elm[1])
print(s)