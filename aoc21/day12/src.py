from collections import defaultdict
lines = open("input.txt").read().strip().splitlines()

G = defaultdict(list)
for l in lines:
    u,v = l.split("-")
    G[u].append(v)
    G[v].append(u)


def solve(node,visited,twice,part2):
    if node in visited and node == node.lower():
        twice = True
    visited_tuple = tuple(sorted(visited))
    if (node,visited_tuple,twice) not in DP:
        if node == "end":
            DP[((node,visited_tuple,twice))] = 1
        else:
            paths = 0
            for u in G[node]:
                if not twice and u not in ["end","start"] and part2:
                    paths += solve(u,visited + [node],twice,part2)
                elif not(u == u.lower() and u in visited ): 
                    paths += solve(u,visited + [node],twice,part2)
            DP[(node,visited_tuple,twice)] = paths
    return DP[(node,visited_tuple,twice)]

DP = {}
ans1 = solve("start",[],False,part2=False)
DP = {}
ans2 = solve("start",[],False,part2=True)

print(ans1)
print(ans2)