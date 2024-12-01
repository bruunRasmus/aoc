import sys
f = open(sys.argv[1],'r')
ins = [l.rstrip().split() for l in f]


def moveTail(head,tail):
    diffX = head[0]-tail[0]
    diffY = head[1]-tail[1]

    if diffY == 0:
        if abs(diffX) > 1:
            tail[0] += (diffX>0)*2 - 1
    elif diffX == 0:
        if abs(diffY) > 1:
            tail[1] += (diffY>0)*2 - 1

    elif (abs(diffY) > 1 or abs(diffX) > 1) and (abs(diffY) >= 1 or abs(diffX) >= 1):
        tail[0] += (diffX>0)*2 - 1
        tail[1] += (diffY>0)*2 - 1

def moveHead(head,dir):
    if dir == 'R':
        head[0]+=1
    if dir == 'L':
        head[0]-=1
    if dir == 'U':
        head[1]+=1
    if dir == 'D':
        head[1]-=1


head = [0,0]
tails = [[0,0] for _ in range(9)]

visited = set()
for i in ins:
    n = int(i[1])
    for j in range(n):
        moveHead(head,i[0])
        moveTail(head,tails[0])
        for k in range(9-1):
            moveTail(tails[k],tails[k+1])
        visited.add((tails[8][0],tails[8][1]))

print(len(visited))
            