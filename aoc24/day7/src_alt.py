import sys
sys.setrecursionlimit(10**8)
with open(sys.argv[1],'r') as f:
    D = f.read().strip().split('\n')

def valid(target,nums):
    if len(nums)==1:
        return nums[0]==target
    return any([valid(target,[nums[0]+nums[1]] + nums[2:]),
                valid(target,[nums[0]*nums[1]] + nums[2:]),
                valid(target,[int(str(nums[0])+str(nums[1]))]+ nums[2:])
                ])
s = 0
for line in D:
    target,rest = line.split(':')
    target = int(target)

    nums = [int(x) for x in rest.strip().split()]
    if valid(target,nums):
        s+=target
print(s)
