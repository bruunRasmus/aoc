import sys
with open(sys.argv[1],'r') as f:
    nums = [[int(x) for x in  (l.rstrip().split(' '))] for l in f]

def safe(xs,j):
    xs  = xs[:j] + xs[j+1:] if j>=0 else xs
    return True not in [xs[i+1]>=xs[i] or xs[i+1]+3<xs[i] for i in range(len(xs)-1)]

s1,s2 = 0,0  
for xs in nums:
    s1+=(safe(xs,-1) or safe(list(reversed(xs)),-1))
    s2+= True in [(safe(xs,i) or safe(list(reversed(xs)),i)) for i in range(len(nums))]
print(s1,s2)