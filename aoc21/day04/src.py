bingo = open("input.txt").read().strip().split("\n\n")

numbers,boards = bingo[0],bingo[1:]

B = [[[[n, False] for n in r.split()] for r in b.splitlines()] for b in boards]
R,C = len(B[0]),len(B[0][0])

won = []
scores = []
for number in numbers.split(","):
    for b in range(len(B)):
        if b in won:
            continue
        board = B[b]
        for row in board:
            for i in range(R):
                n = row[i][0]
                if n == number:
                    row[i][1] = True
                    if sum(row[j][1] for j in range(R))== R  or sum(board[c][i][1] for c in range(C)) == C:
                        s = sum([int(v) for r in board for v,b in r  if not b])
                        won.append(b)
                        scores.append(s*int(n))

print(scores[0])
print(scores[-1])        