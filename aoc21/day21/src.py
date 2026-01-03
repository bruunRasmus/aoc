from functools import cache
p1_pos,p2_pos = [int(l[-1])-1 for l in open("input.txt").read().strip().splitlines()]

@cache
def play(p1_pos, p2_pos, p1_score, p2_score, turn, roll, acc):
    if p1_score >= 21:
        return (1, 0)
    if p2_score >= 21:
        return (0, 1)

    wins1 = wins2 = 0
    if roll == 3:
        if turn == 0:
            new_pos = (p1_pos + acc) % 10
            w1, w2 = play(new_pos, p2_pos,p1_score + new_pos + 1, p2_score,1, 0, 0)
        else:
            new_pos = (p2_pos + acc) % 10
            w1, w2 = play(p1_pos, new_pos,p1_score, p2_score + new_pos + 1,0, 0, 0)
        return (w1, w2)

    for die in (1, 2, 3):
        w1, w2 = play(p1_pos, p2_pos,p1_score, p2_score,turn, roll + 1, acc + die)
        wins1 += w1
        wins2 += w2

    return (wins1, wins2)
ans2 = max(play(p1_pos,p2_pos,0,0,turn = 0,roll= 0, acc= 0))

p1_score = p2_score = turn = 0
while p1_score< 1000 and p2_score <1000:
    turn += 1
    if turn%2 == 1:
        p1_pos = (p1_pos + (turn*3-1)*3)%10
        p1_score += p1_pos + 1
    else:
        p2_pos  = (p2_pos + (turn*3-1)*3)%10
        p2_score += p2_pos + 1

ans1 = turn*3*min(p2_score,p1_score)

print(ans1)
print(ans2)