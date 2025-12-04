import sys
import re
with open(sys.argv[1],'r') as f:
    D = f.read().strip()
    r,p = D.split('\n\n')
    a,b,c = re.findall('\d+',r)
    registerIn = {'A':int(a),'B':int(b),'C':int(c)}
    program = [int(x) for x in re.findall('(\d)+',p)]

def combo(operand,register):
    if operand in range(4):
        return operand
    else:
        return register[['A','B','C'][operand-4]]

def ins(output,pointer,register):
    opcode = program[pointer]
    operand = program[pointer+1]
    pointer += 2
    match opcode:
        case 0: register['A'] =  register['A']//(2**combo(operand,register))
        case 1: register['B'] =  register['B'] ^ operand
        case 2: register['B'] = combo(operand,register)%8
        case 3: 
            if register['A'] == 0:
                pass
            else:
                pointer = operand
        case 4: register['B'] = register['B'] ^ register['C'] 
        case 5: output.append(combo(operand,register)%8)
        case 6: register['B'] =  register['A']//(2**combo(operand,register))
        case 7: register['C'] =  register['A']//(2**combo(operand,register))
    return output,pointer,register

def sim(register):
    output,pointer = [],0
    while pointer < len(program):
        output,pointer,register = ins(output,pointer,register) 
    return output

def solve(v,i):
    if i > len(program):
        return int(v,2)
    for j in range(8):
        bitstring = (v+format(j,'03b'))
        register = {'A':int(bitstring,2),'B':0,'C':0}
        output = sim(register)
        if output == program[-i:]:
            result = solve(bitstring, i + 1)  
            if result: 
                return result
            
print(','.join(map(str,sim(registerIn))))
print(solve('',1))