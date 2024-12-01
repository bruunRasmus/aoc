import sys
f = open(sys.argv[1],'r')

pos = [[[int(z) for z in y.split(',')] 
        for y in x.rstrip().split('@ ')] 
        for x in f.readlines()]

xypairs = [[x[0][0],x[0][0]+x[1][0],x[0][1],x[0][1]+x[1][1]] for x in pos]
abpairs = [[[a,y1-a*x1]for a in [(y2-y1)/(x2-x1)]]for x1,x2,y1,y2 in xypairs]

def intersection(l1,l2,):
    a1,b1 = l1
    a2,b2 = l2
    if a1 == a2:
        return None
    else:
        x = (b2-b1)/(a1-a2)
        y = a1*x + b1
        return (x,y)

def future(x,y,i):
    bx = (x < pos[i][0][0] and pos[i][1][0]<0)  or (x > pos[i][0][0] and pos[i][1][0]>0 )
    by = (y < pos[i][0][1] and pos[i][1][1]<0)  or (y > pos[i][0][1] and pos[i][1][1]>0 )
    return by*bx

minval = 200000000000000
maxval = 400000000000000
s = 0
for i in range(len(abpairs)):
    for j in range(i+1,len(abpairs)):
        try:
            x,y = intersection(abpairs[i][0],abpairs[j][0])
            if minval<=x<=maxval and minval<=y<=maxval and future(x,y,i) and future(x,y,j):
                s+=1
        except:
            pass
print(f"part1: {s}")