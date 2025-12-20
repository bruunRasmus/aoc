lines = list(map(int,open("input.txt").read().strip().splitlines()))

ans1 = ans2 = 0
for i in range(len(lines)-1):
    if ((lines[i+1])>(lines[i])):
        ans1+=1
    if sum(lines[i+1:i+4])>sum(lines[i:i+3]):
        ans2+=1
    
print(ans1)
print(ans2)