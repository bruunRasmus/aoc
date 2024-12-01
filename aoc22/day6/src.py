import sys
f = open(sys.argv[1],'r')

def find_marker(str):
    for i in range(len(str)):
        if len(set(str[i:i+14])) == 14:
            return i+14
        
print([find_marker(s) for s in f])