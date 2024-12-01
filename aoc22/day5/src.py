import sys
import string
from collections import deque 
letters = string.ascii_uppercase

f = open(sys.argv[1],'r')

n = 9
instructions = []
stacks = [deque([]) for _ in range(n)]

for line in f:
    if len(line)>1:
        [stacks[(i-1)//4].appendleft(c) 
            for i,c in enumerate(line.rstrip()) 
            if line[0] != 'm' and c in letters]
        if line[0] == 'm':
            token = line.split()
            instructions.append([int(token[1]),
                                 int(token[3]),
                                 int(token[5])])
    

def move(count,fromStack,toStack):
    items = [stacks[fromStack].pop() for _ in range(count)]
    [stacks[toStack].append(item) for item in reversed(items)]


for i in instructions:
    count,fromStack,toStack = i
    move(count,fromStack-1,toStack-1)
    
for stack in stacks:
    if stack:
        print(stack.pop(),end='')