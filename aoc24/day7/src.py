import sys
from time import time
with open(sys.argv[1],'r') as f:
    input = f.read().strip().split('\n')

baseconversion = 0
valid_check = 0
def base (b,n,l): #convert n to base b, with leading 0's 
    s = time()
    nums = []
    while n:
        n, r = divmod(n, b)
        nums.append(str(r))
    e = time()
    global baseconversion
    baseconversion+=e-s
    return '0'*(l-len(nums)) + ''.join(reversed(nums))

def valid(nums,ops,target):
    global valid_check
    st = time()
    s = nums[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            s+= nums[i+1]
        elif ops[i] == '||':
            s = int(str(s)+str(nums[i+1]))
        else:
            s *= nums[i+1]
        if s>target:
            e = time()
            valid_check += e-st
            return False
    e = time()
    valid_check += e-st
    return s == target

s1,s2 = 0,0
for line in input:
    print("Seconds spent converting to base 3: ",baseconversion)
    print("Seconds spent checking validity: ",valid_check)
    test, rest = line.split(': ')
    nums = [int(x) for x in rest.split()]
    test = int(test)
    ops = ['*','+','||']
    b = len(ops)
    n = len(nums)-1
    
    for i in range(b**(n)):  #number of possible operator combinations
        o = [ops[int(base(b,i,n)[j])] for j in range(n)] #convert index to unique operator combination
        if valid(nums,o,test):
            print(test,nums,o)
            s1+= test if '||' not in o else 0
            s2+=test
            break

print(s1,s2)