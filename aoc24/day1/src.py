import sys
with  open(sys.argv[1],'r') as f:
    a, b = zip(*[(int(x), int(y)) for x, y in (line.rstrip().split('   ') for line in f)])
    a, b = list(sorted(a)), list(sorted(b))

### A ###
print(sum([abs(a[i]-b[i]) for i in range(len(a))]))

### B ###
print(sum(x*sum((x==y) for y in b) for x in a))