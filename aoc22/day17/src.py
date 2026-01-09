from collections import defaultdict
winds = open("input.txt").read().strip().splitlines()[0]

rocks = [[(0,0),(0,1),(0,2),(0,3)],
         [(0,1),(1,0),(1,1),(1,2),(2,1)],
         [(0,0),(0,1),(0,2),(1,2),(2,2)],
         [(0,0),(1,0),(2,0),(3,0)],
         [(0,0),(0,1),(1,0),(1,1)]]
space = [(0,i) for i in range(7)]
SEEN = defaultdict(list)

def fall(space,rock,wind_index,highest_point):
   
    while all(rock_pieces not in space for rock_pieces in rock):
        wind_index = wind_index % len(winds)
        dir = 1 if winds[wind_index] == ">" else -1
        new_rock = [(r,c+dir) for r,c in rock]
        for r,c in new_rock:
            if (r,c) in space or not(0<=c<7):
                break
        else:
            rock = new_rock
        
        wind_index += 1
        rock = [(r-1,c) for r,c in rock]

    space.extend( [(r+1,c) for r,c in rock])
    
    highest_point = max(highest_point,max([r+1 for r,c in rock]))
    top_space = tuple([(r-highest_point + 8,c) for r,c in space if r>=highest_point-8])

    return space,wind_index,highest_point,top_space

stopped = wind_index = highest_point = 0

while stopped < 2022:
    rock_index = stopped%len(rocks)
    rock = rocks[rock_index]
    rock = [(r+highest_point+4,c+2) for (r,c) in rock]
    space,wind_index,highest_point,key = fall(space,rock,wind_index,highest_point)

    if all(i in [c for r,c in key] for i in range(7)):
        SEEN[key].append((stopped,highest_point))
    stopped+=1

print(highest_point)
#1520:2408, 3230:5028, 4940:7648 #cyclelength 1710 addes 2620 blocks
# 2408 + (1000000000000-1520)//1710 * 2620) 
# + increase in height after 3230 + (1000000000000%1710-1520) iters = 4358-2408
print(1532163740808 + 4358-2408)