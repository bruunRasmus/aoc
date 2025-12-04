import sys
from collections import defaultdict
with open(sys.argv[1],'r') as f:
    D = f.read().strip()
    nb = defaultdict(list)
    for l in D.split('\n'):
        a,b = l.split('-')
        nb[a].append(b)
        nb[b].append(a)
        
        
nb = {'a':['aa','b','c'],
      'b':['bb','a','c'],
      'c':['cc','b','a'],
      'aa':['a'],
      'bb':['b'],
      'cc':['c'],}

cliques = []
for v in nb:
    c = [v]
    while True:
        flag = True
        for u in nb:
            if all(u in nb[v] for v in c):
                c.append(u)
                flag = False
        if flag:
            break
    if len(c)>len(cliques):
        cliques = c

print(','.join(sorted(cliques)))