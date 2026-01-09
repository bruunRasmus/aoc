from collections import defaultdict
f = open("input.txt")


s = 'Sensor at x=2, y=18: closest beacon is at x=-2, y=15'

process = lambda lst: [int("".join(numChar)) 
                       for numChar in [[c for c in s if c.isdigit() or c =='-'] 
                            for s  in lst.rstrip().split('=')[1:] ]]


coords = [(process(line)[:2], process(line)[2:]) for line in f]



sensor_interval = defaultdict(list)
N = 4000000
for i,(sensor, beacon) in enumerate(coords):
    print(f"{i}/{len(coords)}")
    b_dist = abs(sensor[0] - beacon[0]) + abs(sensor[1]-beacon[1])
  
    for y in range(max(0,sensor[1]-b_dist),min(N,sensor[1]+b_dist+1)):
        sensor_coverage =  b_dist - abs(sensor[1]-y)
        if sensor_coverage >= 0:
            s_lo,s_hi = sensor[0]-sensor_coverage,sensor[0] + sensor_coverage
            overlapping = []
            for lo,hi in sensor_interval[y]:
                if s_lo - 1 <= hi and s_hi + 1 >= lo:
                    s_lo,s_hi = (min(s_lo,lo),max(s_hi,hi))
                    overlapping.append((lo,hi))
            for i in overlapping:
                sensor_interval[y].remove(i)
            sensor_interval[y].append((max(s_lo,0),min(s_hi,N)))
    

print(sensor_interval)

y = 0

while y <= N:
    x = 0
    while x <= N:
        for sensor,beacon in coords:
            b_dist = abs(sensor[0] - beacon[0]) + abs(sensor[1]-beacon[1])
            p_dist = abs(sensor[0] - x) + abs(sensor[1]-y)
            if p_dist<=b_dist: 
                x =         max(sensor[0] + b_dist - abs(sensor[1]-y) + 1, x)
                break
        else:
            print(x,y)
            print(x*4000000+y)
            break
    y+= 1