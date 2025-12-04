lines = open("input.txt",'r').read().strip()
lines = lines.split("\n")

ans1 = ans2 = 0

dial = 50
for l in lines:
    prev = dial
    direction = ((l[0]=="R")*2-1)
    dial+= int(l[1:])*direction

    ans1 += dial%100 == 0
    ans2 += abs(dial//100 - prev//100) - (prev%100 == 0 and l[0] == "L") + (dial%100 == 0 and l[0] == "L")

print(ans1)
print(ans2)