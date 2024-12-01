import sys
f = open(sys.argv[1],'r')

s = 0
cals = []
for line in f:
    if line == '\n':
        cals.append(s)
        s = 0
    else:
        s+=int(line.rstrip())

print(sum(sorted(cals)[-3:]))
        
