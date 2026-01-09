lines = open("input.txt").read().strip().splitlines()
code_init = [int(x) for x in lines[0].split(",")]

for noun in range(100):
    for verb in range(100):
        code = list(code_init)
        code[1] =noun
        code[2] =verb
        i = 0
        while i < len(code):
            if code[i] == 1:
                code[code[i+3]] = code[code[i+1]]+ code[code[i+2]]
                i+=4 
            elif code[i] == 2:
                code[code[i+3]] = code[code[i+1]]* code[code[i+2]]
                i+=4 
            elif code [i] == 99:
                if code[0] == 19690720:
                    print(100*noun+verb)
                if (noun,verb) == (12,2):
                    print(code[0])
                break

