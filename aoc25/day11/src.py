from collections import defaultdict,deque

lines = open("input.txt",'r').read().strip().split("\n")
G, in_degree = defaultdict(list),defaultdict(int)
ans1 = ans2 = 1

for l in lines:
    vertex,nbs = l.split(":")
    nbs = nbs.split()
    G[vertex] = nbs
    for n in nbs:
        in_degree[n]+=1

TP = [] #topological sort, assumes dag
Q = deque(['svr'])
while Q:
    vertex = Q.popleft()
    TP.append(vertex)
    for nb in G[vertex]:
        in_degree[nb]-=1
        if in_degree[nb] == 0:
            Q.append(nb)

pos = {v: i for i, v in enumerate(TP)}
ordered = sorted(["svr", "fft", "dac", "out"], key=lambda v: pos[v])
pairs = [("you","out")] + list(zip(ordered, ordered[1:]))

for (s,e) in pairs:
    count_from_s = defaultdict(int)
    count_from_s[s] = 1
    for vertex in TP[pos[s]:pos[e]+1]:
        for nb in G[vertex]:
            count_from_s[nb] += count_from_s[vertex]
    if (s,e) == ("you","out"):
        ans1 *= count_from_s[e]
    else:
        ans2*=count_from_s[e]

print(ans1)
print(ans2)