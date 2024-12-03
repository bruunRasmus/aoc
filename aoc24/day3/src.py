import sys
import re
from time import time

with open(sys.argv[1],'r') as f:
    str = f.read()
    
def parse_int(str):
    val = ""
    for j in range(3):
        if str[j].isnumeric(): val+=str[j]
        else: break
    return val
####
preLoop = time()
####
s1,s2 = 0,0
enable = True

for i in range(len(str)-1):
    if str[i:i+4]=='do()':
        enable = True
    if str[i:i+7]=='don\'t()':
        enable = False
    offset = i+4
    if str[i:offset] == 'mul(':
        a = parse_int(str[offset:])
        if str[offset+len(a)] == ',':
            b = parse_int(str[offset+len(a)+1:])
            if str[offset+len(a)+1+len(b)] == ")":
                s1 += int(a)*int(b)
                s2 += int(a)*int(b) * enable
                
print(f'part 1: {s1}')        
print(f'part 2: {s2}') 

####
postLoop = time()
####

s1,s2 = 0,0
enable = True
r = "mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"

for a,b,do,dont in re.findall(r,str):
    if do or dont:
        enable = bool(do)
    else:
        s1 += int(a)*int(b)
        s2 += int(a)*int(b) * enable

print(f'part 1: {s1}')        
print(f'part 2: {s2}') 

####
postReg = time()
####
print(f'Time for loop: \t{postLoop-preLoop:.4f}')
print(f'Time for regex:\t{postReg-postLoop:.4f}')