import sys
with open(sys.argv[1],'r') as f:
    D = f.read().strip()
    G, ins = D.split('\n\n')
    GG = G.split('\n')
    ins = ins.replace('\n','')
    
def g2(grid):
    return [list(row.replace('#', '##')
                  .replace('O', '[]')
                  .replace('.', '..')
                  .replace('@', '@.')) for row in grid]

for part2 in [False,True]:
    G = g2(GG) if part2 else [list(row) for row in GG]
    R,C = len(G),len(G[0])

    for r in range(R):
        for c in range(C):
            if G[r][c] == '@':
                subr,subc = r,c

    dir = {'<':[0,-1],'v':[1,0],'>':[0,1],'^':[-1,0]}
    for i in ins:
        stack = [[(subr,subc)]]
        dr,dc = dir[i]
        
        while all([G[pr+dr][pc+dc] != '#' for pr,pc in stack[-1]]):
            if all((G[pr+dr][pc+dc] == '.' for pr,pc in stack[-1])):
                break
            else:
                if i in ['<','>']:
                    for pr,pc in stack[-1]:
                        stack.append([(pr+dr,pc+dc)])
                        if part2:
                            stack.append([(pr+2*dr,pc+2*dc)])
                else:
                    b = set()
                    for pr,pc in stack[-1]:
                        if G[pr+dr][pc+dc] == '[':
                            b.add((pr+dr,pc+dc))
                            b.add((pr+dr,pc+dc+1))
                        elif G[pr+dr][pc+dc] == ']':
                            b.add((pr+dr,pc+dc))
                            b.add((pr+dr,pc+dc-1))
                        elif G[pr+dr][pc+dc] == 'O':
                            b.add((pr+dr,pc+dc))
                    stack.append(list(b))

        if any(G[pr+dr][pc+dc] == '#' for pr,pc in stack[-1]):
            continue

        n = len(stack)
        for i in range(n):
            for j in range(len(stack[n-i-1])):
                r,c = stack[n-i-1][j]
                temp = G[r][c]
                G[r][c] = '.'
                G[r+dr][c+dc] = temp
        subr,subc = subr+dr,subc+dc
    
    s = sum(100 * r + c for r in range(R) for c in range(C) if G[r][c] not in ['.','#',']','@'])
    print(s)