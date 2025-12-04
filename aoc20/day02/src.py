import sys
with open(sys.argv[1],'r') as f:
    D = f.read().strip().split('\n')

s1,s2= 0,0
for line in D:
    tokens = line.split(' ')
    low,high = map(int,tokens[0].split('-'))

    char = tokens[1][0]
    str = tokens[2]

    if low<=str.count(char)<=high:
        s1+=1
    s2 += (str[low-1] == char) ^ (str[high -1] == char)
print(s1,s2)
