import sys
f = open(sys.argv[1],'r')

digplan = [l.rstrip().split(' ') for l in f.readlines()]
part2 = False if sys.argv[2] == '1' else True

P = [[0,0]] #start vertex
s = 0 #length of boundary
for d in digplan:
    x,y = P[-1]
    if part2:
        v = int('0x'+d[2][2:-2],16) 
        dir =  d[2][-2]
    else:
        v = int(d[1])
        dir = d[0]
    s+=v
    if dir in ['0','R']:
            P.append([x+v,y])
    elif dir in ['2','L']:
            P.append([x-v,y])
    elif dir in ['3','U']:
            P.append([x,y-v])
    else:
            P.append([x,y+v])
            
xs = [x for x,_ in P]
ys = [y for _,y in P]
xmin = min(xs)
ymin = min(ys)
xmax = max(xs)
ymax = max(ys)

x1,y1= P[0]
ss = 0
n = len(P)
for i in range(n+1): 
    x2,y2 = P[i%n]
    ss += (x1*y2-y1*x2)
    x1,y1 = x2,y2
    
print(ss/2 + s/2 + 1) #why div 2?? ss area of poly, s "area" of "boundary"