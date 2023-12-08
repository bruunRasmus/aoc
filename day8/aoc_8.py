import sys

f = open(sys.argv[1],'r')

def rlToInt (rlstring):
    return [1 if (c == 'R') else 0 for c in rlstring]

rl = rlToInt(f.readlines(2)[0].rstrip())
d = {}
for l in f:
    if l[0].isalpha():
        d[l[:3]] = [l.split("(")[1][:3],l[-5:-2]]

current = 'AAA'
i = 0
while current != 'ZZZ':
    for walk in rl:
        if current != 'ZZZ':
            current = d[current][walk]
            print(current)
            i+=1
        else:
            break
print(i)
