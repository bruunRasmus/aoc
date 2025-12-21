from collections import defaultdict
lines = open("input.txt").read().strip().splitlines()

G = defaultdict(list)
for l in lines:
    u,v = l.split("-")
    G[u].append(v)
    G[v].append(u)
    
DP = {}
def solve(node = "start",visited = [],twice = False,part2 = False):
    if node in visited and node == node.lower():
        twice = True
    visited_tuple = tuple(sorted(visited))
    if (node,visited_tuple,twice,part2) not in DP:
        if node == "end":
            DP[((node,visited_tuple,twice,part2))] = 1
        else:
            paths = 0
            for u in G[node]:
                if not twice and u not in ["end","start"] and part2:
                    paths += solve(u,visited + [node],twice,part2)
                elif not(u == u.lower() and u in visited ): 
                    paths += solve(u,visited + [node],twice,part2)
            DP[(node,visited_tuple,twice,part2)] = paths
    return DP[(node,visited_tuple,twice,part2)]

ans1 = solve(part2=False)
ans2 = solve(part2=True)

print(ans1)
print(ans2)