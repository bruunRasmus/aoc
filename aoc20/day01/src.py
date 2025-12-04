import sys
with open(sys.argv[1],'r') as f:
    D = [int(x) for x in f.read().strip().split('\n')]
    
for x in D:
    for y in D:
        for z in D:
            if x+y+z == 2020:
                print(x*y*z)