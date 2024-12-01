import sys
import numpy as np
f = open(sys.argv[1],'r')

forrest = np.array([[int(c) for c in l.rstrip()] for l in f])


R = len(forrest)
C = len(forrest[0])

viewable = 2*R + 2*C - 4
for r in range(1,R-1):
    for c in range(1,C-1):
        height = forrest[r][c]
        peak = min(
            max(forrest[r,c+1:]),
            max(forrest[r,:c]),
            max(forrest[r+1:,c]),
            max(forrest[:r,c]))
        if height > peak:
            viewable += 1


def scenic(h,lst):
    for i in range(len(lst)):
        if lst[i]>=h:
            return i + 1
    return len(lst)

scenic_score = 0
for r in range(1,R-1):
    for c in range(1,C-1):
        height = forrest[r][c]
        score = 1
        score *= scenic(height,forrest[r,c+1:]) 
        score *= scenic(height,list(reversed(forrest[r,:c]))) 
        score *= scenic(height,forrest[r+1:,c]) 
        score *= scenic(height,list(reversed(forrest[:r,c])))
 
        scenic_score = max(scenic_score,score)
print(scenic_score)
print(viewable)