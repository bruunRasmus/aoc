lines = open("input.txt").read().strip().splitlines()

pos = [int(x) for x in lines[0].split(",")]

ans1 = ans2 = max(pos)*max(pos)*len(pos)
for pe in range(max(pos)):
    dist1 = dist2 = 0
    for ps in pos:
        d = (abs(pe-ps))
        dist1 += d
        dist2 += (d+1)*(d/2)
    ans1 = min(ans1,dist1)
    ans2 = min(ans2,dist2)
print(ans1)
print(ans2)