import sys
sys. setrecursionlimit(100000)
f = open(sys.argv[1],'r')

cubes = [[int(x) for x in l.split(',')] for l in f]

def neighbour_count(cubeA,lst):
    c = 0 
    for cubeB in lst:
        c +=  sum([abs(cubeA[i] - cubeB[i]) for i in range(len(cubeA))])  == 1
    return c

area = 0
for i in range(len(cubes)):
    cur = cubes[i]
    rest = cubes[i+1:]
    area += 6 - 2*(neighbour_count(cur,rest))
print(area)


high = max([max(x) for x in cubes])


def nb_points(point):
    x,y,z = point
    return[[x+1,y,z],
           [x-1,y,z],
           [x,y+1,z],
           [x,y-1,z],
           [x,y,z-1],
           [x,y,z+1]]

print("2",area- 6*((high+1)**3 - 3106-len(cubes)))
points = []
def fill(seed):
    #print("seed",seed)
    global points
    if max(seed)>high or min(seed)<0:
        return
    print(len(points))
    if seed in cubes or seed in points:
        return
    else:
        if seed not in points:
            points.append(seed)
        for nb in nb_points(seed):
            fill(nb)


#fill([high,high,high])


print("yo")
print(area- 6*((high+1)**3 - len(points)-len(cubes)))

