import sys
f = open(sys.argv[1],'r')

ins = [l.rstrip().split() for l in f]

count = 1
cycle = 0


interesting_cycles = [40*x+20 for x in range(6)]
interesting_values = []

def inc():
    global cycle

    if (cycle)%40 in [count-1,count,count+1]:
        print('#',end = '')
    else:
        print('.',end = '')

    cycle += 1
    if cycle  in interesting_cycles:
        interesting_values.append(count*cycle)

    if cycle%40 == 0:
        print()
    

for i in ins:
    if i[0] == 'noop':
        inc()
    elif i[0] == 'addx':
        inc()
        inc()
        count += int(i[1])

print(sum(interesting_values))