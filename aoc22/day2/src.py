import sys
f = open(sys.argv[1],'r')


p1 = {'A':0,'B': 1,'C':2}
p2 = {'X':0,'Y': 1,'Z':2}

def score (case):
    opp,you = case
    return ((p2[you]-p1[opp] + 1 )% 3)*3 + p2[you]+1

def result(case):
    opp,res = case

    you =  (p1[opp]+ p2[res] - 1) % 3 + 1
    point = (p2[res])*3

    return you + point
    
print(sum([result(l.rstrip().split()) for l in f]))