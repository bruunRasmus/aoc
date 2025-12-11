import pulp
solver = pulp.PULP_CBC_CMD(msg=False)
lines = open("input.txt",'r').read().strip().split("\n")

machines = []
for l in lines:
    target,remaining = l.split("]")
    target = [0 if t == "." else 1 for t in target[1:] ]
    buttons,remaining = remaining.split("{")
    wiring = []
    for b in buttons.split():
        flip = [0 for _ in range(len(target))]
        for c in b:
            if c not in ["(",",",")"]:
                flip[int(c)] = 1
        wiring.append(flip)
    joltage = [int(c) for c in remaining[:-1].split(",")]
    machines.append((target,wiring,joltage))

ans1 = ans2 =  0
for target,buttons,joltage in machines:
    n_buttons = len(buttons)
    n_targets = len(target)

    X1 = [pulp.LpVariable(f"button_{i}", lowBound=0, upBound=1, cat=pulp.LpInteger) for i in range(len(buttons))]
    model1 = pulp.LpProblem("indicator_lights", pulp.LpMinimize)
    model1 += pulp.lpSum([X1[i] for i in range(n_buttons)])
    
    for i in range(len(target)):
        k = pulp.LpVariable(f"k_{i}", lowBound=0, cat="Integer")
        model1 += (
            pulp.lpSum(buttons[j][i] * X1[j] for j in range(n_buttons))
            == target[i] + 2 * k
    )

    model1.solve(solver)
    ans1+= int(pulp.value(model1.objective))

    ###-------------------------------------------------------------------------------------------------------###

    X2 = [pulp.LpVariable(f"button_{i}", lowBound=0, cat=pulp.LpInteger) for i in range(len(buttons))]
    model2 = pulp.LpProblem("indicator_lights", pulp.LpMinimize)
    model2 += pulp.lpSum([X2[i] for i in range(n_buttons)])

    for i in range(len(joltage)):
        model2 += (
            pulp.lpSum([buttons[j][i]* X2[j] for j in range(len(buttons))])
            == joltage[i] 
    )
    model2.solve(solver)
    ans2+= int(pulp.value(model2.objective))

print(ans1)
print(ans2)