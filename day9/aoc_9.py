import sys
f = open(sys.argv[1],'r')

oasis1 = [[int(x) for x in line.split()] for line in f]
oasis2 = [list(reversed(line)) for line in oasis1]

def next(line):
    length = len(line)
    for i in range(length):
        for j in range(length-i-1):
            line[j] = line[j+1]-line[j]
    return sum(line) 
            
print(sum(next(line) for line in oasis1))
print(sum(next(line) for line in oasis2))