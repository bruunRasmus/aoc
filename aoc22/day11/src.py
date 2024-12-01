import sys
import math
f = open(sys.argv[1],'r')

n = 8

M = [[[],[],[],[]] for _ in range (n)]
inspectCount = [0 for _ in range(n)]

currentM = -1
for line in f:
    line = line.split()

    if len(line) == 0:
        pass
    elif line[0] =='Monkey':
        currentM +=1
    elif line[0] =='Starting':
        for val in line[2:]:
            M[currentM][0].append(int(val[:2]))
    elif line[0] == 'Operation:':
        M[currentM][1] = line[-3:]
    elif line[0] == 'Test:':
        M[currentM][2] = [int(line[-1])]
    elif line[1] =='true:':
        M[currentM][3].append(int(line[-1]))
    elif line[1] =='false:':
        M[currentM][3].append(int(line[-1]))

divs = [m[2][0] for m in M]
LCM = math.lcm(*divs)

def throw(item, fromMonkey, toMonkey ):
    #print(f'item with worry level {item} is thrown from  {fromMonkey} to {toMonkey}')
    M[fromMonkey][0].pop(0)
    M[toMonkey][0].append(item)

def inspect(monkey,operation,a,b):
    inspectCount[monkey] += 1
    if operation == '+':
        return (a + b) % LCM
    elif operation == '*':
        return (a * b) % LCM


def round():
    for monkey in range(n):
        items = M[monkey][0]
        a,operation,b = M[monkey][1]
        div = M[monkey][2][0]
        true,false = M[monkey][3]

        for _ in range(len(items)):
            left =  items[0] if a =='old' else int(a)
            right =  items[0] if b =='old' else int(b)
            new = inspect(monkey,operation,left,right)
            
            if new%div == 0:
                throw (new,monkey,true)
            else:
                throw (new,monkey,false)
        
for _ in range(10000):
    round()


level = sorted(inspectCount)
print(inspectCount)
print(level[-2]*level[-1])