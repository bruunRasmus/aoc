import sys
f = open(sys.argv[1],'r')

oasis = [list(reversed([int(x) for x in line.split()])) for line in f]

s = 0
for line in oasis:
    length = len(line)
    for i in range(length):
        for j in range(length-i-1):
            line[j] = line[j+1]-line[j]
    s += sum(line)
print(s)   