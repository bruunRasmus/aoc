import heapq
from collections import defaultdict
import itertools
counter = itertools.count()

lines =  open("input.txt").read().strip().splitlines()
G = [list(l) for l in lines]
hallway = {}
rooms = defaultdict(list)

R,C = len(G),len(G[0])
amphi2room = {"A":3,"B":5,"C":7,"D":9}
room2amphi = {3:"A",5:"B",7:"C",9:"D"}
amphicost = {"A":1,"B":10,"C":100,"D":1000}

for r in range(R):
    for c in range(C):
        if c <len(G[r]):
            if r ==  1 and  G[r][c] in ["A","B","C","D","."]:
                hallway[c] = G[r][c]
            if r >  1 and G[r][c] in ["A","B","C","D"]:
                rooms[c].append(G[r][c])

DEPTH_ROOMS = len(rooms[3])

def valid_new_states(cost,state):
    new_states = []
    hallway,rooms = state
    for c in hallway:
        occupant = hallway[c]
        if occupant == ".": 
            continue
        amphi_room = amphi2room[occupant]
        if all(ra == occupant for ra in rooms[amphi_room]):
            route = sorted([c,amphi_room])
            
            if all(hallway[i] ==  "." for i in range(route[0]+1,route[1])):
                new_hallway = dict(hallway)
                new_hallway[c] = "."
                new_rooms = {k: list(v) for k, v in rooms.items()}
                new_rooms[amphi_room].append(occupant)
                new_cost = cost + (route[1]-route[0] + DEPTH_ROOMS + 1-len(new_rooms[amphi_room]))*amphicost[occupant]
                new_states.append((new_cost,(new_hallway,new_rooms)))
    for c in rooms:
        if all(o == room2amphi[c] for o in rooms[c]):
            continue
        for i in range(c+1,12):
            if hallway[i] != ".":
                break
            if i in room2amphi:
                continue
            else:
                new_rooms = {k: list(v) for k, v in rooms.items()}
                amphi = new_rooms[c][0]
                new_rooms[c].remove(amphi)
                new_hallway = dict(hallway)
                new_hallway[i] = amphi
                new_cost = cost + (i-c + DEPTH_ROOMS-len(new_rooms[c]))*amphicost[amphi]
                new_states.append((new_cost,(new_hallway,new_rooms)))
        for i in range(c-1,0,-1):
            if hallway[i] != ".":
                break
            if i in room2amphi:
                continue
            else:
                new_rooms = {k: list(v) for k, v in rooms.items()}
                amphi = new_rooms[c][0]
                new_rooms[c].remove(amphi)
                new_hallway = dict(hallway)
                new_hallway[i] = amphi
                new_cost = cost + (c-i + DEPTH_ROOMS-len(new_rooms[c]))*amphicost[amphi]
                new_states.append((new_cost,(new_hallway,new_rooms)))
    return new_states

Q = [(0,0,(hallway,rooms))]
heapq.heapify(Q)
seen = set()

while Q:
    cost,_,state = heapq.heappop(Q)
    h,r = state
    for room in r:
        if not(all(amphi== room2amphi[room] for amphi in r[room]) and len(r[room]) == DEPTH_ROOMS):
            break
    else:
        print(cost,state)
        break
       
    print(cost)
    for new_cost,new_state in valid_new_states(cost,state):
        hashable_state = (new_cost,
            tuple(sorted((k, tuple(v)) for k, v in new_state[0].items())),
            tuple(sorted((k, tuple(v)) for k, v in new_state[1].items()))
        )

        if hashable_state in seen:
            continue
        else:
            seen.add(hashable_state)
        heapq.heappush(Q,(new_cost,next(counter),new_state))