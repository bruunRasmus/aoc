import sys
import itertools
sys.setrecursionlimit(10**9)
with open(sys.argv[1],'r') as f:
    D = f.read().strip().split('\n')
    
pad = {'<': (0,2),'v':(0,1),'>':(0,0),'^':(1,1),'A':(1,0)}
num = {'A': (0,0),'0':(0,1),
       '1':(1,2),'2':(1,1),'3':(1,0),
       '4':(2,2),'5':(2,1),'6':(2,0),
       '7':(3,2),'8':(3,1),'9':(3,0),}

def sp(a,b):
    if a in num and b in num:   return sp_num(a,b)
    else:                       return sp_pad(a,b)
def sp_num(a,b):
    (ar,ac),(br,bc) = num[a],num[b]

    c = ['<','>'][bc<ac]
    r = ['^','v'][br<ar]

    if (ar,ac) in [(0,0),(0,1)] and bc == 2:
        retval = [r*abs(br-ar)+c*abs(bc-ac)]
    
    elif (br,bc) in [(0,0),(0,1)] and ac == 2:
        retval = [c*abs(bc-ac)+r*abs(br-ar)]
    elif br == ar or bc == ac:
        retval = [r*abs(br-ar)+c*abs(bc-ac)]
    else:
        retval = [c*abs(bc-ac)+r*abs(br-ar),
              r*abs(br-ar)+c*abs(bc-ac)]
    return retval

def sp_pad(a,b):
    (ar,ac),(br,bc) = pad[a],pad[b]

    c = '<' if bc < ac else '>'
    r = '^' if br < ar else 'v'
    if (ar,ac) == (0,2):
        retval = [c*abs(bc-ac)+r*abs(br-ar)]
    elif (br,bc) == (0,2):
        retval = [r*abs(br-ar)+c*abs(bc-ac)]
    elif br == ar or bc == ac:
        retval = [r*abs(br-ar)+c*abs(bc-ac)]
    else:
        retval = [c*abs(bc-ac)+r*abs(br-ar),
              r*abs(br-ar)+c*abs(bc-ac)]
    return retval

dp = {}
def solve(depth, seq):
    if depth == 0:
        return len(seq) - 1
    if (depth, seq) not in dp:
        pos_combs = [sp(seq[i], seq[i+1]) for i in range(len(seq) - 1)]
        ns = sum(
            min(solve(depth - 1, 'A' + comb + 'A') for comb in comb_i)
            for comb_i in pos_combs
            )
        dp[(depth, seq)] = ns
    return dp[(depth, seq)]

ans1,ans2 = 0,0
for seq in D:
    seq = 'A' + seq
    ans1 += solve(3,seq)*int(seq[1:4])
    ans2 += solve(27,seq)*int(seq[1:4])
    
print(ans1,ans2)