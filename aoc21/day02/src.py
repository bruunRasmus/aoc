lines = open("input.txt").read().strip().splitlines()

pos = [0,0,0]

for l in lines:
    dir,n = l.split()
    if dir == "forward":
        pos[0]+=int(n)
        pos[2]+=int(n)*pos[1]
    if dir == "up":
        pos[1]-=int(n)
    if dir == "down":
        pos[1]+=int(n)

ans1 = pos[0]*pos[1]
ans2 = pos[2]*pos[0]
print(ans1)
print(ans2)