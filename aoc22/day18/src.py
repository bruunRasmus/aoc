from collections import deque
f = open("input.txt")

cubes = [tuple([int(x) for x in l.split(',')]) for l in f]

def neighbour_count(cubeA,lst):
    c = 0 
    for cubeB in lst:
        c +=  sum([abs(cubeA[i] - cubeB[i]) for i in range(len(cubeA))])  == 1
    return c

ans1 = ans2 = 0
for i in range(len(cubes)):
    cur = cubes[i]
    rest = cubes[i+1:]
    ans1 += 6 - 2*(neighbour_count(cur,rest))

high = max([max(x) for x in cubes])
Q = deque([(high,high,high)])
seen = set()
while Q:
    x,y,z = Q.popleft()
    if not(0-1<=x<=high+1 and 0-1<=y<=high+1 and 0-1<=z<=high+1):
        continue
    for dx,dy,dz in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
                xx,yy,zz = x+dx,y+dy,z+dz
                if (xx,yy,zz) in cubes:
                    ans2+=1
                elif (xx,yy,zz) not in seen:
                    seen.add((xx,yy,zz))
                    Q.append((xx,yy,zz))
print(ans1)
print(ans2)