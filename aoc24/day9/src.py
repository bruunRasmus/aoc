import sys
from copy import deepcopy
with open(sys.argv[1],'r') as f:
    D = f.read().strip()

disk_orig = []
c = {}
for i in range(len(D)):
    n = int(D[i])
    if i%2 == 1:
        for j in range(n):
            disk_orig.append('.')
    else:
        for j in range(n):
            disk_orig.append(int(i)//2)
        c[int(i)//2] = n

for part2 in [False, True]:
    disk = disk_orig[:]
    n = len(disk_orig)
    s = 0
    i = n - 1
    while i > s:
        if disk[i] != '.':
            b = c[disk[i]] if part2 else 1
            j = s
            while i > j:
                if all(disk[j + k] == '.' for k in range(b)): 
                    disk[j:j + b], disk[i - b + 1:i + 1] = disk[i - b + 1:i + 1], ['.'] * b
                    break
                j += 1
        i -= 1
    print(sum([(i)*int(disk[i]) for i in range(n) if disk[i]!= '.']))
        




