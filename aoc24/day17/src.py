import sys
import re
with open(sys.argv[1],'r') as f:
    D = f.read().strip()
    r,p = D.split('\n\n')
    a,b,c = re.findall('\d+',r)
    
    register = {'A':int(a),'B':int(b),'C':int(c)}
    program = [int(x) for x in re.findall('(\d)+',p)]

pointer = 0


def combo(operand):
    if operand in range(4):
        return operand
    else:
        return register[['A','B','C'][operand-4]]


def ins(opcode,operand):
    global pointer
    global output 
    pointer += 2
    if opcode ==  0:
        register['A'] =  register['A']//(2**combo(operand))
    if opcode == 1:
        register['B'] =  register['B'] ^ operand
    if opcode == 2:
        register['B'] = combo(operand)%8
    if opcode == 3:
        if register['A']== 0:
            pass
        else:
            pointer = operand
    if opcode == 4:
        register['B'] = register['B'] ^ register['C'] 
    if opcode == 5:
        output.append(combo(operand)%8)
    if opcode == 6:
        register['B'] =  register['A']//(2**combo(operand))
    if opcode == 7:
        register['C'] =  register['A']//(2**combo(operand))
i = 0
while i > -1:
    if i % 100000 ==0:
        print(i)
    output = []
    pointer = 0
    register['A'] = i
    while pointer < len(program):
        if output != program[:len(output)]:
            break
        ins(program[pointer],program[pointer+1])
    
    if output == program:
        print(i)
        break
    i+=1
    

