import sys
import string
f = open(sys.argv[1],'r')

#rss = [(sorted(list(set(l[:len(l)//2]))),sorted(list(set(l[len(l)//2:-1])))) for l in f]
rss2 = [set(l.rstrip()) for l in f]


def identify_identical(common,lsts):
        for l in lsts:
            common_mod = [c for c in l if c in common]
            common = common_mod
        return common
                    
vals = {i:c+1 for (c,i) in enumerate (string.ascii_letters)}
common = [ (identify_identical(string.ascii_letters,rss2[3*i:3*i+3])) for i in range(len(rss2)//3) ]

print(sum([vals[c] for cc in common for c in cc]))