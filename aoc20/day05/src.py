import sys
with open(sys.argv[1],'r') as f:
    D = f.read().strip().split('\n')

s=0
filled = []
for line in D:
    
    lowR,highR = 0,127
    lowC,highC = 0,7

    for c in line[:7]:
        if c =='F':
            highR -= (highR-lowR+1)//2
        else:
            lowR += (highR-lowR+1)//2
    for c in line[7:]:
        if c =='R':
           lowC += (highC-lowC+1)//2
          
        else:
            highC -= (highC-lowC+1)//2
    filled.append(((lowR)*8+lowC))
    s = max(((lowR)*8+lowC),s)
print(s)

for i in range(max(filled)):
    if i not in filled:
        if i+1 in filled and i-1 in filled:
            print(i)
            break


