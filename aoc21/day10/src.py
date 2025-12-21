from collections import deque
lines = open("input.txt").read().strip().splitlines()
valid = {"(":")","{":"}","[":"]","<":">"}
points1 = {")":3,"]":57,"}":1197,">":25137}
points2 = {"(":1,"[":2,"{":3,"<":4}

ans1 = 0
scores = []
for l in lines:
    Q = deque()
    for c in l:
        if c in valid:
            Q.appendleft(c)
        else:
            tbc = Q.popleft()
            if c != valid[tbc]:
                ans1+=points1[c]
                break   
    else:
        score = 0
        while Q:
            c = Q.popleft()
            score *= 5
            score += points2[c]
        scores.append(score)

ans2 = sorted(scores)[len(scores)//2]
print(ans1)
print(ans2)