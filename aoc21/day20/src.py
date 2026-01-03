enhancement, image = open("input.txt").read().strip().split("\n\n")
G = [list(l) for l in image.splitlines()]

def extend(G,fill = "."):
    G = [[fill] + r + [fill] for r in G]
    G = [[fill for _ in range(len(G[0]))]] + G + [[fill for _ in range(len(G[0]))] ]
    R,C = len(G),len(G[0])
    return G,R,C

def enhance(G,i):
    fill = "." if i%2 == 0 else "#"
    G,R,C = extend(G,fill=fill)
    G_enh = [["." for _ in range(R)] for _ in range(C)]
    for r in range(R):
        for c in range(C):
            new_value = ""
            for dr in [-1,0,1]:
                for dc in [-1,0,1]:
                    rr = r+dr
                    cc = c+dc
                    if 0<=rr<R and 0<=cc<C:
                        new_value += "1" if  G[rr][cc] == "#" else "0"
                    else:
                        new_value += "0" if i%2 == 0 else "1"
            i = int(new_value,2)
            G_enh[r][c] = enhancement[i]
    return G_enh

G,_,_ = extend(G)
ans1 = ans2 = 0

for i in range(50):
    if i == 2:
        ans1 = sum((G[r][c] == "#" for r in range(len(G)) for c in range(len(G[0]))))

    G = enhance(G,i)
    
ans2 = sum((G[r][c] == "#" for r in range(len(G)) for c in range(len(G[0]))))

print(ans1)
print(ans2)