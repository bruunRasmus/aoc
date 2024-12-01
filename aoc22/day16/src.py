import sys
from time import time
from collections import deque, defaultdict

sys.setrecursionlimit(10000)
f = open(sys.argv[1],'r')

flows = {}
neighbours = {}


#Preprocess
for l in f:
    tokens = l.split()
    flows[tokens[1]] = int((tokens[4].split('=')[-1])[:-1])
    
    if 'valve' in tokens:
        neighbours[tokens[1]] = [tokens[-1]]
    else:
        neighbours[tokens[1]] = []
        for v in reversed(tokens):
            if v == 'valves':
                break
            else:
                neighbours[tokens[1]].append(v[:2])


def bfs_shortest_path(adj_list, start):
    # Dictionary to store shortest path distances
    shortest_path = {node: float('inf') for node in adj_list}
    shortest_path[start] = 0
    
    # Queue for BFS
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        
        # Visit each neighbor
        for neighbor in adj_list[current]:
            if shortest_path[neighbor] == float('inf'):  # Unvisited node
                shortest_path[neighbor] = shortest_path[current] + 1
                queue.append(neighbor)
    
    return shortest_path

shortest_paths = {k:bfs_shortest_path(neighbours,k) for k in flows.keys()}

configs = {}
configs2 = {}
posFlows = {k:v for (k,v) in flows.items() if v > 0}
N = len(posFlows.keys())

def step(prevFlow,nodeYou,nodeElephant,opened,t):
    youStep,youOpen,eleStep,eleOpen,retval = [[] for _ in range(5)]

    if nodeYou not in opened and flows[nodeYou]>0:
        flowYou = flows[nodeYou]*(t-1)
        youOpen = [nodeYou]
        youStep.append([flowYou,nodeYou,youOpen])
    if (nodeElephant not in opened and nodeElephant not in youOpen) and flows[nodeElephant]>0:
        flowElephant = flows[nodeElephant]*(t-1)
        eleOpen = [nodeElephant]
        eleStep.append([flowElephant,nodeElephant,eleOpen])
    for nbYou in neighbours[nodeYou]:
        youStep.append([0,nbYou,[]])
    for nbEle in neighbours[nodeElephant]:
        eleStep.append([0,nbEle,[]])

    for flowYou,newNodeYou,newOpenYou in youStep:
        for flowEle,newNodeEle,newOpenEle in eleStep:
            newFlow = prevFlow+flowEle+flowYou
            newOpened = opened+newOpenYou+newOpenEle
            retval.append([newFlow,newNodeYou,newNodeEle,newOpened,t-1])
    
    return retval


def value(node,opened,t):
    setOpened = ''.join(sorted(opened))
    if t <= 0 or len(opened) == N:
        return 0
    elif (node,setOpened,t) in configs.keys():
            return configs[((node,setOpened,t))]
    else:
        if node not in opened and flows[node]>0:
            tunnel = flows[node]*(t-1)
            otherOpen = max([value(nb,opened+[node],t-2) for nb in neighbours[node]])
        else:
            tunnel = 0
            otherOpen = 0
        otherLeave = max([value(nb,opened,t-1) for nb in neighbours[node]])

        configs [(node,setOpened,t)] = max(tunnel+otherOpen,otherLeave)
        return configs[(node,setOpened,t)]


maxFlow = 0

def earlyStop(prevFlow,nodeYou,nodeElephant,opened,t):
    if t<=0:
        return True
    elif len(opened) == N:
        return True
    else: 
        global maxFlow
        remainingValves = sorted([(k,v) for k,v in posFlows.items()  if k not in opened],key=lambda x:x[1],reverse=True)
        posRemFlow = 0
        for valve,flow in remainingValves:
            spYou = shortest_paths[nodeYou][valve]
            spEle = shortest_paths[nodeElephant][valve]
            sp = min(spYou,spEle)
            posRemFlow += flow*(t-sp)
        if prevFlow+posRemFlow<maxFlow:
            return True
        else:
            return False
def valueElephant(prevFlow,nodeYou,nodeElephant,opened,t):
    setOpened = ''.join(sorted(opened))
    if earlyStop(prevFlow,nodeYou,nodeElephant,opened,t):
        global maxFlow
        if prevFlow>maxFlow:
            maxFlow=prevFlow
            #print(opened)
            #print(maxFlow)
        return prevFlow
    elif (nodeYou,nodeElephant,setOpened,t) in configs2.keys():
        return configs2[((nodeYou,nodeElephant,setOpened,t))]
    elif (nodeElephant,nodeYou,setOpened,t) in configs2.keys():
        return configs2[((nodeElephant,nodeYou,setOpened,t))]
    else:
        newStates = step(prevFlow,nodeYou,nodeElephant,opened,t)
        star = max([valueElephant(*state) for state in newStates])

        configs2[nodeYou,nodeElephant,setOpened,t] =star
        return configs2[nodeYou,nodeElephant,setOpened,t]
        
start = time()        
print(value('AA',[],30))
print(valueElephant(0,'AA','AA',[],26))
end = time()
print(f'Elapsed time: {end-start}')