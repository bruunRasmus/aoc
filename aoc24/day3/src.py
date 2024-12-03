import sys
with open(sys.argv[1],'r') as f:
    str = f.read()
    
def parse_int(str):
    val = ""
    for j in range(3):
        if str[j].isnumeric(): val+=str[j]
        else: break
    return val

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