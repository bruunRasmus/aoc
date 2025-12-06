from operator import add,mul

lines = open("input.txt",'r').read().split("\n")[:-1]
lines = [list(line) for line in lines]
lines = [l + [" "] * (len(lines[0]) - len(l) + 1) for l in lines]

R,C = len(lines),len(lines[0])

ops = {"*":(mul,1),"+":(add,0)}
ans1 = ans2 = 0

nums = []
for c in range(C):
    val = "".join(lines[r][c] for r in range(R-1))
    if lines[R-1][c] != " ": op,unit = ops[lines[R-1][c]]
    
    if val.strip():
        nums.append(val)
    else:
        res2 = unit
        for n in nums:
            res2 = op(res2,int(n))
        ans2+= res2

        res1 = unit
        for i in range(len(nums[0])):
            val = "".join([n[i] for n in nums])
            res1 = op(res1,int(val))
        ans1+=res1

        nums = []

print(ans1)
print(ans2)