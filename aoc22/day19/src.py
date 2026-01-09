
from functools import cache

blueprints = open("input.txt").read().strip().splitlines()

blueprint_costs = []
for b in blueprints:
    
    c = [int(x) for x in b.split() if x.isdigit()]
    costs = ((c[0],0,0,0),(c[1],0,0,0),(c[2],c[3],0,0),(c[4],0,c[5],0))
    blueprint_costs.append(costs)

@cache
def geode(time_left,resources, robots, costs):
    global best
  
    max_needed = [max(costs[i][j] for i in range(4)) for j in range(4)]
    best_possible = resources[3] + robots[3] * (time_left ) + (time_left ) *(time_left-1)//2 
    potential_total = resources[3] + robots[3]* time_left

    if time_left == 0 or best_possible < best:
        return potential_total
    
    best_for_branch = potential_total

    for i in range(4):
        if i != 3 and max_needed[i] <= robots[i]:
            continue

        can_build = all(robots[j]>=1 for j in range(4) if costs[i][j] >= 1)
        wait_time = 0
        for j in range(3):
            if robots[j] == 0:
                continue
            if costs[i][j] > resources[j]:
                needed = costs[i][j] - resources[j]
                turns = (needed + robots[j] - 1) // robots[j] #trick in case of common factor
                wait_time = max(wait_time, turns)

        if can_build and wait_time  < time_left - 1:
            new_time = time_left-wait_time - 1
            new_resources = tuple([resources[j] + robots[j]*(wait_time+1)  - costs[i][j] for j in range(4)])
            new_robots = tuple([robots[j]+ (j==i) for j in range(4)])
            
            best_for_branch = max(geode(new_time,new_resources,new_robots,costs),best_for_branch)
            best = max(best,best_for_branch)
    
    return best_for_branch

ans1 = 0
ans2 = 1
for i,costs in enumerate(blueprint_costs):
    best = 0
    ans1 += (i+1)*geode(24,(0,0,0,0),(1,0,0,0),costs)
    if i <3: ans2 *= geode(32,(0,0,0,0),(1,0,0,0),costs)

print(ans1)
print(ans2)