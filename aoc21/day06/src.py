lines = open("input.txt").read().strip().splitlines()

DP = {}
def solve(timer,days):
    if (timer,days) not in DP: 
        if days == 0:
            return 1
        else:
            if timer == 0:
                DP[(timer,days)] = solve(6,days-1) + solve(8,days-1)
            else:
                DP[(timer,days)] = solve(timer-1,days-1)
    return DP[(timer,days)]

ans1 = ans2 = 0
for s in lines[0].split(","):
    ans1 += solve(int(s),80)
    ans2 += solve(int(s),256)
print(ans1)
print(ans2)