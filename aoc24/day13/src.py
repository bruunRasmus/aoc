import sys
import re
with open(sys.argv[1],'r') as f:
    D = f.read().strip()
    games = D.split('\n\n')
    
config = [[int(x) for x in (re.findall('\d+',g))] for g in games]

for part2 in [False,True]:
    s = 0
    for a1,a2,b1,b2,c1,c2 in config:
        if part2:
            c1 += 10000000000000
            c2 += 10000000000000
  
        x2 = (c2-((a2/a1)*c1))/(b2-((a2/a1)*b1))
        x1 = (c1-(b1*x2))/a1

        x1,x2 = round(x1),round(x2)
        if (x1*a1+x2*b1,x1*a2+x2*b2) == (c1,c2):
            s += 3*x1+x2
    print(s)
