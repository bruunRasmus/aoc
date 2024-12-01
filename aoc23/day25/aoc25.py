import sys
import random
import copy
from math import prod
f = open(sys.argv[1],'r')

wires = [l.rstrip().split(':') for l in f.readlines()]
wiresD = {w[0]:set(w[1].split()) for w in wires}

Vs = set()
Es = set()
for w in wiresD:
    Vs.add(w)
    for ww in wiresD[w]:
        Vs.add(ww)
        Es.add(tuple(sorted((w,ww))))
Vl = {v:1 for v in Vs}
El = [list(e) for e in Es]

#2-approx for min-cut
def contract(E,V):
    while len(V)> 2:
        print(len(V))
        e = random.choice(E)
        E.remove(e)
        V[e[0]] += V[e[1]]
        del V[e[1]]
        E = [sorted([e[0],e2]) if e1 == e[1] else (e1,e2)  for e1,e2 in E ]
        E = [sorted([e[0],e1]) if e2 == e[1] else (e1,e2)  for e1,e2 in E ]
        while ([e[0],e[0]]) in E:
            E.remove([e[0],e[0]])
    return E,V

while True:
    VV = copy.deepcopy(Vl)
    EE = copy.deepcopy(El)
    cut = (contract(EE,VV))
    #if the solution min-cut is the only of size 3, the
    # p(|approx-min-cut| = 3) > 2/(1526*(1526 - 1)) = 0,00000085
    # so after 806528 iteration p(|approx-min-cut|>3 for all i) < 0.5 
    # but bound is worst-case, avg. found after 200 iters.
    if len(cut[0]) == 3: #if min-cut
        print(prod(cut[1].values()))
        break