import sys
import numpy as np
from scipy.sparse import csr_matrix

f = open(sys.argv[1],'r')

stepmap = [l.rstrip() for l in f.readlines()]
R = len(stepmap)
C = len(stepmap[0])

def neighbours(r,c):
    retval = []
    for n in [[0,1],[0,-1],[1,0],[-1,0]]:
        rr =r+n[0]
        cc = c+n[1]
        if 0<=rr<R and 0<=cc<C:
            retval.append([rr,cc])
    return retval

N = []

for r in range(R):
    for c in range(C):
        if stepmap[r][c] == 'S':
            S = [r,c]
        if stepmap[r][c] in ['.','S']:
            
            for n in neighbours(r,c):
                rr,cc = n
                if stepmap[rr][cc] == '.':
                    N.append([r*C+c,rr*C+cc])
        
A = np.zeros([R*C,R*C])
for n in N:
    r,c = n
    A[r,c] = 1
    A[c,r] = 1

#horribly slow O((C*R)^2*2,37*64)   
Asparse = csr_matrix(A)
A64 = Asparse**64
CS = A64[S[0]*C+S[1]]
print("64:",np.count_nonzero(CS.todense()))