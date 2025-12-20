groups = open("input.txt").read().strip().split("\n\n")

ans1 = ans2 = 0

for g in groups:
    y = {}
    for member in g.splitlines():
        for question in member:
            if question in y:
                y[question] += 1
            else:
                y[question] = 1
    ans1 += len(y)
    for q in y:
        if y[q] == len(g.splitlines()):
            ans2+=1

print(ans1)
print(ans2)