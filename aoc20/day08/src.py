instructions =  open("input.txt").read().strip().splitlines()

value = i = 0
seen = set()

while True:
    if i in seen:
        break
    seen.add(i)
    ins,v = instructions[i].split()
    
    v = int(v[1:]) if v[0] == "+" else -int(v[1:])

    if ins == "acc":
        value += v
        i+=1
    if ins == "jmp":
        i+= v
    if ins == "nop":
        i+= 1

print(value)