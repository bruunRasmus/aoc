lines = open("input.txt").read().strip().splitlines()

ans1 = ans2 = 0

for l in lines:
    fuel = int(l)//3-2
    ans1+= fuel
    ans2+=fuel
    while fuel>0:
        fuel = fuel//3-2
        ans2+=max(fuel,0)
print(ans1)
print(ans2)